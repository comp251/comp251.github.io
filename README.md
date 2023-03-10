# COMP251 Spring 23 Course Website

## Credit and License

* Theme is derived from [Just the
  Docs](https://just-the-docs.github.io/just-the-docs/).
* SCSS for the `module` class (for `dl`, `dt`, `dd`) in [](_scss/custom) from
  [Just the Class](https://kevinl.info/just-the-class/).

## About

* Uses `git submodule` for lab assignments, see `submodule_bootstrap.sh` for
  initial adding of subtrees and `submodule_update.sh` to update local clones.
* `run_local.sh` will run Jekyll locally. Follow installation instructions for
  [Jekyll](https://jekyllrb.com/) as a prerequisite.
* Syllabus is pulled from [\_data/days.yaml](_data/days.yaml).
* Announcements are pulled from
  [\_data/announcements.yaml](_data/announcements.yaml). The `date` field is
  when the announcement expires.
* [\_data/gen\_schedule.yaml](_data/gen_schedule.py) is a poorly-written python
  script to generate the syllabus dates.
* To run locally, use:
  
  ``` $ ./run_local.sh $ ./run_local.sh -H hostname-to-listen-on ```

## TODO

* [_layouts/default.html]() and [_includes/nav.html]() are workarounds for an
  issue with external nav links. See
  [this PR](https://github.com/just-the-docs/just-the-docs/pull/1001) for
  details. __remove when 0.4.0 is released.__

