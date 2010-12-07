# Instagram JSONP Proxy and embed example

I want to embed my [Instagram][] photo stream in [My blog][my_blog]. But for now, the only way is using the iPhone app.

So I introduce this hacking instagram jsonp proxy server and some JavaScript/HTML/CSS code to prove this prossibility.
[Instagram][] said they are working on a public API, but it's not available yet.
You can figure out their private API schema by TCPDUMP, so did I.
The purpose of this project is *NOT* for:

* fetch popular photos;
* get user info;
* convert username to user id (or searching a user);

The only purpose is:

* backup yor photostream (you should find out your user_id first);
* expose this photostream as jsonp api;
* embed code for showing your photostream anywhere;

Mislav Marohnić kindly provide a [unofficial Instagram API][mislav_instagram_wiki] wiki, I think it's a better place to know what beneath the great instagram app.

## Usage

  Run this app on localhost by ./manage.py runserver 0.0.0.0:8000
  Browse http://localhost:8000/front/index.html , you can see my photostream (my instagram id is diamondtin)

## Living Example

  Visit my blog: http://www.diamondtin.com
  It's on the bottom of the sidebar

[instagram]: http://instagr.am/
[mislav_instagram_wiki]: https://github.com/mislav/instagram/wiki "Instagram API"
[my_blog]: http://www.diamondtin.com