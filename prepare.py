"""Auto script to create files for the project."""

import os
import pathlib

import yaml

cores = [
    "window_size",
    "broadcast_channel",
    "mouse",
    "resize_observer",
    "active_element",
    "clipboard",
    "event_listener",
    "preferred_contrast",
    "notification",
    "image",
    "element_bounding",
    "permission",
    "useragent",
    "mutation_observer",
    "drop_zone",
    "dom_visible",
    "text_direction",
    "favicon",
    "window_focus",
    "media_query",
    "window_scroll",
    "fps",
    "wake_lock",
    "fullscreen",
    "preferred_dark",
    "intersection_observer",
    "file_dialog",
    "async_state",
    "object_url",
    "preferred_reduced_motion",
    "geolocation",
    "breakpoints",
    "preferred_languages",
    "element_size",
    "websocket",
    "memory",
    "raf_fn",
    "network",
    "worker",
    "eye_dropper",
    "supported",
]

integrations = ["qr_code", "change_case", "jwt"]

shareds = [
    "adjust_with_unit",
    "try_on_destroy",
    "throttle_fn",
    "unstore",
    "interval_fn",
    "debounce_fn",
    "date_format",
    "watchable",
    "toggleable",
    "to_writable",
    "to_string",
    "timeout",
    "tryit",
    "timeout_fn",
    "sleep",
    "to_number",
    "create_singleton_promise",
    "to_readable",
    "counter",
    "type",
    "args_flat",
    "last_changed",
    "slug",
    "try_get_current_component",
    "create_event_hook",
    "make_destructurable",
    "interval",
    "len",
    "utils",
    "range",
    "template",
]


shareds_curry = ["chain", "partial", "compose"]

shareds_dicts = [
    "shake",
    "picker",
    "listify",
    "enhance",
    "pops",
    "map_values",
    "map",
    "invert",
    "contains",
]


shareds_lists = [
    "last",
    "count",
    "list",
    "merge",
    "flat",
    "cluster",
    "group",
    "enhance",
    "fork",
    "unique",
    "intersects",
    "select",
    "sort",
    "sift",
    "first",
]

shareds_math = [
    "random",
    "average",
    "sum",
    "create_projection",
    "create_generic_pojection",
    "min",
    "max",
    "projection",
    "precision",
    "clamp",
]

core_path = pathlib.Path(__file__).parent.absolute().joinpath("docs", "core")


integrations_path = (
    pathlib.Path(__file__).parent.absolute().joinpath("docs", "integrations")
)


shareds_path = pathlib.Path(__file__).parent.absolute().joinpath("docs", "shared")

shareds_curry_path = (
    pathlib.Path(__file__).parent.absolute().joinpath("docs", "shared", "curry")
)


shareds_dicts_path = (
    pathlib.Path(__file__).parent.absolute().joinpath("docs", "shared", "dicts")
)

shareds_lists_path = (
    pathlib.Path(__file__).parent.absolute().joinpath("docs", "shared", "lists")
)


shareds_math_path = (
    pathlib.Path(__file__).parent.absolute().joinpath("docs", "shared", "math")
)


for core in cores:
    if f"{core}.md" not in os.listdir(core_path):
        with open(core_path.joinpath(f"{core}.md"), "w") as f:
            f.write(f'# {core.replace("_", " ").title()}')


for integration in integrations:
    if f"{integration}.md" not in os.listdir(integrations_path):
        with open(integrations_path.joinpath(f"{integration}.md"), "w") as f:
            f.write(f'# {integration.replace("_", " ").title()}')


for shared in shareds:
    if f"{shared}.md" not in os.listdir(shareds_path):
        with open(shareds_path.joinpath(f"{shared}.md"), "w") as f:
            f.write(f'# {shared.replace("_", " ").title()}')

for shared_curry in shareds_curry:
    if f"{shared_curry}.md" not in os.listdir(shareds_curry_path):
        with open(shareds_curry_path.joinpath(f"{shared_curry}.md"), "w") as f:
            f.write(f'# {shared_curry.replace("_", " ").title()}')

for shared_dicts in shareds_dicts:
    if f"{shared_dicts}.md" not in os.listdir(shareds_dicts_path):
        with open(shareds_dicts_path.joinpath(f"{shared_dicts}.md"), "w") as f:
            f.write(f'# {shared_dicts.replace("_", " ").title()}')

for shared_lists in shareds_lists:
    if f"{shared_lists}.md" not in os.listdir(shareds_lists_path):
        with open(shareds_lists_path.joinpath(f"{shared_lists}.md"), "w") as f:
            f.write(f'# {shared_lists.replace("_", " ").title()}')

for shared_math in shareds_math:
    if f"{shared_math}.md" not in os.listdir(shareds_math_path):
        with open(shareds_math_path.joinpath(f"{shared_math}.md"), "w") as f:
            f.write(f'# {shared_math.replace("_", " ").title()}')


mkdocs = {}

with open("./mkdocs.yml", "r") as f:
    mkdocs = yaml.load(f, Loader=yaml.FullLoader)


nav: list = mkdocs["nav"]

for n in nav:

    if n.get("Integrations"):
        _integrations: list[dict] = n["Integrations"]

        values = [
            value.split(".")[1].split("/")[-1]
            for elem in _integrations
            for value in elem.values()
        ]

        for integration in integrations:
            if integration not in values:
                _integrations.append(
                    {
                        integration.replace(
                            "_", " "
                        ).title(): f"./integrations/{integration}.md"
                    }
                )
        _integrations.sort(key=lambda x: list(x.keys())[0])

    if n.get("Core"):
        _core: list[dict] = n["Core"]

        values = [
            value.split(".")[1].split("/")[-1]
            for elem in _core
            for value in elem.values()
        ]

        for core in cores:
            if core not in values:
                _core.append({core.replace("_", " ").title(): f"./core/{core}.md"})
        _core.sort(key=lambda x: list(x.keys())[0])

    if n.get("Shared"):
        _shared: list[dict] = n["Shared"]

        _shared_list: list[dict] = _shared.pop(
            _shared.index([x for x in _shared if x.get("Lists")][0])
        ).get("Lists")

        _shared_dict: list[dict] = _shared.pop(
            _shared.index([x for x in _shared if x.get("Dicts")][0])
        ).get("Dicts")

        _shared_math: list[dict] = _shared.pop(
            _shared.index([x for x in _shared if x.get("Math")][0])
        ).get("Math")

        _shared_curry: list[dict] = _shared.pop(
            _shared.index([x for x in _shared if x.get("Curry")][0])
        ).get("Curry")

        values = [
            value.split(".")[1].split("/")[-1]
            for elem in _shared
            for value in elem.values()
        ]

        lists_values = [
            value.split(".")[1].split("/")[-1]
            for elem in _shared_list
            for value in elem.values()
        ]

        dicts_values = [
            value.split(".")[1].split("/")[-1]
            for elem in _shared_dict
            for value in elem.values()
        ]

        math_values = [
            value.split(".")[1].split("/")[-1]
            for elem in _shared_math
            for value in elem.values()
        ]

        curry_values = [
            value.split(".")[1].split("/")[-1]
            for elem in _shared_curry
            for value in elem.values()
        ]

        for shareds_list in shareds_lists:
            if shareds_list not in lists_values:
                _shared_list.append(
                    {
                        shareds_list.replace(
                            "_", " "
                        ).title(): f"./shared/lists/{shareds_list}.md"
                    }
                )

        for shareds_dict in shareds_dicts:
            if shareds_dict not in dicts_values:
                _shared_dict.append(
                    {
                        shareds_dict.replace(
                            "_", " "
                        ).title(): f"./shared/dicts/{shareds_dict}.md"
                    }
                )

        for shareds_math in shareds_math:
            if shareds_math not in math_values:
                _shared_math.append(
                    {
                        shareds_math.replace(
                            "_", " "
                        ).title(): f"./shared/math/{shareds_math}.md"
                    }
                )

        for curry in shareds_curry:
            if curry not in curry_values:
                _shared_curry.append(
                    {curry.replace("_", " ").title(): f"./shared/curry/{curry}.md"}
                )

        _shared_list.sort(key=lambda x: list(x.keys())[0])

        _shared_dict.sort(key=lambda x: list(x.keys())[0])

        _shared_math.sort(key=lambda x: list(x.keys())[0])

        _shared_curry.sort(key=lambda x: list(x.keys())[0])

        _shared.append({"Lists": _shared_list})

        _shared.append({"Dicts": _shared_dict})

        _shared.append({"Math": _shared_math})

        _shared.append({"Curry": _shared_curry})

        for shared in shareds:
            if shared not in values:
                _shared.append(
                    {shared.replace("_", " ").title(): f"./shared/{shared}.md"}
                )
        _shared.sort(key=lambda x: list(x.keys())[0])


with open("./mkdocs.yml", "w") as f:
    yaml.dump(mkdocs, f, sort_keys=False)
