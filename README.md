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
usage: markov.py [-h] [filename] [minlen] [eta_s] [handles]

positional arguments:
  filename    Destination to training-data
  minlen      Minimum length to try
  eta_s       Minimum observation it must have made
  handles     Add <s> </s> handles to output
  
optional arguments:
  -h, --help  show this help message and exit
  ```

e.g.
> python3 ~/markov/markov.py ~/.weechat/logs/irc.underworld.no.#foobar.weechatlog 10 2 n
