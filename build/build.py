import sass
from staticjinja import Site
import os
import htmlmin

if __name__ == "__main__":
    sass.compile(dirname=("sass/", "../assets/css/"), output_style='compressed')
    site = Site.make_site(outpath="../",
                        #   env_globals={'greeting':'Hello world!',}
                          )
    site.render()
    # os.rename("../index.jinja","../index.html")
    htmlmin.minify('../index.html')
    with open('../index.jinja', 'r') as jinja_file:
                content = htmlmin.minify(jinja_file.read(),
                                         remove_empty_space=True,
                                         remove_comments=True)
    if os.path.exists('../index.html'):
        os.remove('../index.html')
    os.remove('../index.jinja')
    with open('../index.html', 'w') as html_file:
        html_file.write(content)

