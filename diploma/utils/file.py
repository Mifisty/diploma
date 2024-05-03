def abs_path_from_project(relative_path: str):
    import diploma
    from pathlib import Path

    return (
        Path(diploma.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
