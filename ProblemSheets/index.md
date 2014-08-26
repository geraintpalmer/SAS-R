---
layout : default
title  : 'Problem Sheets'
---

The problem sheets for the course contain lists of questions that will be presented (by the students) during contact time.

{% for page in site.pages %}
    {% if page.categories contains 'problemsheet' %}
- [{{ page.title }}]({{ page.url | prepend: site.baseurl }})
    {% endif %}
{% endfor %}

There are a variety of question types:

1. Challenges (specific questions aimed to help cover the corresponding content of the course);
2. Practice questions;
3. Past assessment.

