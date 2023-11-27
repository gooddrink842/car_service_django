def check_is_completed(parts_to_service):
    is_not_completed = False
    for part_to_service in parts_to_service:
        if (not part_to_service.is_approved) and (not part_to_service.is_rejected):
            is_not_completed = True
    return not is_not_completed