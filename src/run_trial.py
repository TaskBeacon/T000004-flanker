from functools import partial

from psyflow import StimUnit, set_trial_context

# trial stages use task-specific phase labels via set_trial_context(...)
_TRIAL_COUNTER = 0


def _next_trial_id() -> int:
    global _TRIAL_COUNTER
    _TRIAL_COUNTER += 1
    return _TRIAL_COUNTER


def _deadline_s(value) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, (list, tuple)) and value:
        try:
            return float(max(value))
        except Exception:
            return None
    return None


def run_trial(
    win,
    kb,
    settings,
    condition: str,
    stim_bank: dict,
    trigger_runtime=None,
    block_id=None,
    block_idx=None,
):
    """Run one Flanker trial."""
    trial_id = _next_trial_id()
    trial_data = {"condition": condition}
    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    flanker_type, target_direction = condition.split("_")
    correct_response = settings.left_key if target_direction == "left" else settings.right_key

    trial_data.update(
        {
            "flanker_type": flanker_type,
            "target_direction": target_direction,
            "correct_response": correct_response,
        }
    )

    # phase: pre_stim_fixation
    fixation_unit = make_unit(unit_label="fixation").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        fixation_unit,
        trial_id=trial_id,
        phase="pre_stim_fixation",
        deadline_s=_deadline_s(settings.fixation_duration),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=str(condition),
        task_factors={
            "condition": str(condition),
            "stage": "pre_stim_fixation",
            "flanker_type": flanker_type,
            "target_direction": target_direction,
            "block_idx": block_idx,
        },
        stim_id="fixation",
    )
    fixation_unit.show(
        duration=settings.fixation_duration,
        onset_trigger=settings.triggers.get("fixation_onset"),
    ).to_dict(trial_data)

    # phase: flanker_response
    stim_unit = make_unit(unit_label="stimulus").add_stim(stim_bank.get(condition))
    set_trial_context(
        stim_unit,
        trial_id=trial_id,
        phase="flanker_response",
        deadline_s=_deadline_s(settings.stim_duration),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=str(condition),
        task_factors={
            "condition": str(condition),
            "stage": "flanker_response",
            "flanker_type": flanker_type,
            "target_direction": target_direction,
            "correct_key": str(correct_response),
            "block_idx": block_idx,
        },
        stim_id=str(condition),
    )
    stim_unit.capture_response(
        keys=settings.key_list,
        correct_keys=correct_response,
        duration=settings.stim_duration,
        response_trigger={
            settings.left_key: settings.triggers.get("left_key_press"),
            settings.right_key: settings.triggers.get("right_key_press"),
        },
        onset_trigger=settings.triggers.get(f"{flanker_type}_stim_onset"),
        terminate_on_response=True,
    )
    stim_unit.to_dict(trial_data)

    # outcome display
    response = stim_unit.get_state("response", False)
    hit = stim_unit.get_state("hit", False)

    if response and hit:
        feedback_stim = stim_bank.get("correct_feedback")
        feedback_trigger = settings.triggers.get("feedback_correct_response")
    elif response and not hit:
        feedback_stim = stim_bank.get("incorrect_feedback")
        feedback_trigger = settings.triggers.get("feedback_incorrect_response")
    else:
        feedback_stim = stim_bank.get("no_response_feedback")
        feedback_trigger = settings.triggers.get("feedback_no_response")

    make_unit(unit_label="feedback").add_stim(feedback_stim).show(
        duration=settings.feedback_duration,
        onset_trigger=feedback_trigger,
    ).to_dict(trial_data)

    make_unit(unit_label="iti").show(duration=settings.iti_duration).to_dict(trial_data)

    return trial_data
