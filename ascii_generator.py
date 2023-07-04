def generate_ascii_art(text, style):
    if style == 'standard':
        return text
    elif style == 'shadow':
        return r"""
   .=-.-.      _ __                    .=-.-.         ,-.-.   .=-.-.                    ,----.
 /==/_ /   .-`.' ,`.    _,..---._    /==/_ /  ,--.-./=/ ,/  /==/_ /   _,..---._     ,-.--` , \
|==|, |   /==/, -   \ /==/,   -  \  |==|, |  /==/, ||=| -| |==|, |  /==/,   -  \   |==|-  _.-`
|==|  |  |==| _ .=. | |==|   _   _\ |==|  |  \==\,  \ / ,| |==|  |  |==|   _   _\  |==|   `.-.
|==|- |  |==| , '=',| |==|  .=.   | |==|- |   \==\ - ' - / |==|- |  |==|  .=.   | /==/_ ,    /
|==| ,|  |==|-  '..'  |==|,|   | -| |==| ,|    \==\ ,   |  |==| ,|  |==|,|   | -| |==|    .-'
|==|- |  |==|,  |     |==|  '='   / |==|- |    |==| -  ,/  |==|- |  |==|  '='   / |==|_  ,`-._
/==/. /  /==/ - |     |==|-,   _`/  /==/. /    \==\  _ /   /==/. /  |==|-,   _`/  /==/ ,     /
`--`-`   `--`---'     `-.`.____.'   `--`-`      `--`--'    `--`-`   `-.`.____.'   `--`-----``

"""
    elif style == 'slant':
        return r"""
                     ___        _____                                              _____          ___
    ___          /  /\      /  /::\       ___           ___        ___         /  /::\        /  /\
   /  /\        /  /::\    /  /:/\:\     /  /\         /__/\      /  /\       /  /:/\:\      /  /:/_
  /  /:/       /  /:/\:\  /  /:/  \:\   /  /:/         \  \:\    /  /:/      /  /:/  \:\    /  /:/ /\
 /__/::\      /  /:/~/:/ /__/:/ \__\:| /__/::\          \  \:\  /__/::\     /__/:/ \__\:|  /  /:/ /:/_
 \__\/\:\__  /__/:/ /:/  \  \:\ /  /:/ \__\/\:\__   ___  \__\:\ \__\/\:\__  \  \:\ /  /:/ /__/:/ /:/ /\
    \  \:\/\ \  \:\/:/    \  \:\  /:/     \  \:\/\ /__/\ |  |:|    \  \:\/\  \  \:\  /:/  \  \:\/:/ /:/
     \__\::/  \  \::/      \  \:\/:/       \__\::/ \  \:\|  |:|     \__\::/   \  \:\/:/    \  \::/ /:/
     /__/:/    \  \:\       \  \::/        /__/:/   \  \:\__|:|     /__/:/     \  \::/      \  \:\/:/
     \__\/      \  \:\       \__\/         \__\/     \__\::::/      \__\/       \__\/        \  \::/
                 \__\/                                   ~~~~                                 \__\/

"""
