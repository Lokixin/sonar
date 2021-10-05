class EmojiToEmoticon(object):
    '''
    Mappings from emoji to emoticon
    '''

    def __init__(self) -> None:
        self.mappings ={
            'o/' :'👋',
            '</3' :'💔',
            '<3' :'💗',
            '8-D' :'😁',
            '8D' :'😁',
            ':-D' :'😁',
            '=-3' :'😁',
            '=-D' :'😁',
            '=3' :'😁',
            '=D' :'😁',
            'B^D' :'😁',
            'X-D' :'😁',
            'XD' :'😁',
            'x-D' :'😁',
            'xD' :'😁',
            ':\')' :'😂',
            ':\'-)' :'😂',
            ':-))' :'😃',
            '8)' :'😄',
            ':)' :'😄',
            ':-)' :'😄',
            ':3' :'😄',
            ':D' :'😄',
            ':]' :'😄',
            ':^)' :'😄',
            ':c)' :'😄',
            ':o)' :'😄',
            ':}' :'😄',
            ':っ)' :'😄',
            '=)' :'😄',
            '=]' :'😄',
            '0:)' :'😇',
            '0:-)' :'😇',
            '0:-3' :'😇',
            '0:3' :'😇',
            '0;^)' :'😇',
            'O:-)' :'😇',
            '3:)' :'😈',
            '3:-)' :'😈',
            '}:)' :'😈',
            '}:-)' :'😈',
            '*)' :'😉',
            '*-)' :'😉',
            ':-,' :'😉',
            ';)' :'😉',
            ';-)' :'😉',
            ';-]' :'😉',
            ';D' :'😉',
            ';]' :'😉',
            ';^)' :'😉',
            ':-|' :'😐',
            ':|' :'😐',
            ':(' :'😒',
            ':-(' :'😒',
            ':-<' :'😒',
            ':-[' :'😒',
            ':-c' :'😒',
            ':<' :'😒',
            ':[' :'😒',
            ':c' :'😒',
            ':{' :'😒',
            ':っC' :'😒',
            '%)' :'😖',
            '%-)' :'😖',
            ':-P' :'😜',
            ':-b' :'😜',
            ':-p' :'😜',
            ':-Þ' :'😜',
            ':-þ' :'😜',
            ':Þ' :'😜',
            ':þ' :'😜',
            ';(' :'😜',
            '=p' :'😜',
            'X-P' :'😜',
            'd:' :'😜',
            'x-p' :'😜',
            ':-||' :'😠',
            ':@' :'😠',
            ':-.' :'😡',
            ':-/' :'😡',
            ':\\' :'😡',
            '=L' :'😡',
            '=\\' :'😡',
            ':\'(' :'😢',
            ':\'-(' :'😢',
            '^5' :'😤',
            '^<_<' :'😤',
            'o/\\o' :'😤',
            '|-O' :'😫',
            '|;-)' :'😫',
            ':###..' :'😰',
            ':-###..' :'😰',
            'D-\':' :'😱',
            'D:<' :'😱',
            'D=' :'😱',
            'v.v' :'😱',
            '8-0' :'😲',
            ':-O' :'😲',
            ':-o' :'😲',
            ':O' :'😲',
            ':o' :'😲',
            'O-O' :'😲',
            'O_O' :'😲',
            'O_o' :'😲',
            'o-o' :'😲',
            'o_O' :'😲',
            'o_o' :'😲',
            ':$' :'😳',
            '#-)' :'😵',
            ':#' :'😶',
            ':&' :'😶',
            ':-#' :'😶',
            ':-&' :'😶',
            ':-X' :'😶',
            ':X' :'😶',
            ':-J' :'😼',
            ':*' :'😽',
            ':^*' :'😽',
            'ಠ_ಠ' :'🙅',
            '*\\0/*' :'🙆',
            '\\o/' :'🙆',
            ':>' :'😄',
            '>.<' :'😡',
            '>:(' :'😠',
            '>:)' :'😈',
            '>:-)' :'😈',
            '>:/' :'😡',
            '>:O' :'😲',
            '>:P' :'😜',
            '>:[' :'😒',
            '>:\\' :'😡',
            '>;)' :'😈',
            '>_>^' :'😤',
        }

        self.emoji_set = set(self.mappings.keys())
        self.emoticon_set = set(self.mappings.values())

    def convert(self, text: str) -> str:
        '''
        replaces emojis with emoticons in a piece of text
        '''
        for token in text.split(" "):
            if token in self.emoji_set:
                text = text.replace(token, self.mappings[token])
        return text