---
title: Home
layout: home
nav_order: 0
---

# {{ site.description }}

* Instructor: Dr. Marion Lang
  * Email: [langm@rhodes.edu](mailto:langm@rhodes.edu)
  * My Calendar: [Lang Rhodes Public](https://tinyr.us/lang-cal); book time
    using [calendly.com/langma](https://calendly.com/lang-cal)
* __This website:__ [https://ml8.github.com/comp251]() (alternate link
  [http://251.systems]())
* [CS Program Slack](https://rhodes-cs.slack.com): `#comp251-sp23`
* [Feedback](https://forms.gle/74oBX4KXSBuonmvh8)
* [Code from class](https://github.com/rhodes-comp251-fa22/code-from-class)

{% if site.data.announcements %}

{% if site.data.announcements.first.date > site.time %}

{: .announcement }
{{ site.data.announcements.first.text }}

{% endif %}
{% endif %}


## Course Schedule

<div class="module" markdown="1">
{% for date in site.data.days %}

{{ date.day_name }} {{ date.month }}/{{ date.day }}
: {% if date.topic %} {{ date.topic }} {% else %} \- {% endif %}
{% if date.reading %}: {{ date.reading }} {% endif %}
{% if date.assignment %}: {{ date.assignment }} {% endif %}

{% endfor %}
</div>
