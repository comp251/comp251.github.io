---
title: Home
layout: home
nav_order: 0
---

# {{ site.description }}

* Instructor: Dr. Marion Lang
  * Email: [langm@rhodes.edu](mailto:langm@rhodes.edu)
  * [My calendar](https://tinyr.us/lang-cal); book time
    using [calendly.com/langma](https://calendly.com/lang-cal)
* This website: [comp251.github.io](https://comp251.github.io)/[251.systems](http://251.systems)
* [CS Program Slack](https://rhodes-cs.slack.com): `#comp251`

{% for ann in site.data.announcements %}
{% if ann.date > site.time %}
{: .announcement }
{{ ann.text }}
{% endif %}
{% endfor %}

## Course Schedule

<div class="module" markdown="1">

{% for date in site.data.days %}

{{ date.day_name }} {{ date.month }}/{{ date.day }}

: {{ date.topic | default: "&nbsp;" }}
  : {% if date.reading %}{{ date.reading }}{% endif %}
  : {% if date.assignment %}{{ date.assignment }}{% endif %}

{% endfor %}

</div>
