# Markov
## Markov Chain for Weechat-logs

### License:
```
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
```

### How to run:
```
usage: markov.py [-h] [-m [number]] [-e [number]] [-nh] [--version]
                 [/path/to/data]

positional arguments:
  /path/to/data         Path to training-data (Required)

optional arguments:
  -h, --help            show this help message and exit
  -m [number], --minlen [number]
                        Minimum sentence length to try (Not guaranteed)
  -e [number], --eta-s [number]
                        Minimum amount of observations required
  -nt, --no-tags        Remove "<s> </s>" tags from output
  --version             Print version info
  ```

e.g.
> python3 ~/markov/markov.py ~/.weechat/logs/irc.underworld.no.#foobar.weechatlog -m 10 -e 2 --no-tags

### What is this?
This project is inspired by [/r/subredditsimulator](https://www.reddit.com/r/SubredditSimulator/). For an explanation, click [here](https://www.reddit.com/r/SubredditSimulator/comments/3g9ioz/what_is_rsubredditsimulator/)
