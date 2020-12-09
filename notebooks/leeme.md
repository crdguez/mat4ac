```shell
pandoc -s -t pdf resumen_2ev.md -o prueba.pdf -V geometry:landscape,margin=0.2in -V documentclass:report -V toc -V lang=es
```

Usar YAML:

---
title: "The Document Title"
author: [Example Author, Another Author]
date: "2017-02-20"
keywords: [Markdown, Example]
titlepage: true
geometry: landscape,margin=0.2in
...
