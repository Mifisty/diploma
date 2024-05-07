def abs_path_from_project(relative_path: str):
    import kazanexpress_project_api_mobile_ui
    from pathlib import Path

    return (
        Path(kazanexpress_project_api_mobile_ui.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
