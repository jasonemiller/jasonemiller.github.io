---
title:  How to set up pagination in jekyll's minima theme
author: jason
date:  2020-12-24
tags: coding jekyll
---

found this page

https://despinouy.github.io/jekyll/minima/blogging/development/english/2019/06/27/jekyll-minima.html

added 'jekyll-paginate' to Gemfile and _config.yml

at prompt, ran gem install jekyll-pagination

in _config.yml
paginate:  7
   - paginate-path:"blog/page-:num/"

 ran bundle install

 https://stackoverflow.com/questions/57659321/how-to-paginate-in-jekyll

 pagineate excertps

 https://blog.yipl.com.np/jekyll-pagination-2bc8a52221b3