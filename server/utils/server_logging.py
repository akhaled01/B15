from rich.console import Console
import datetime

class Logger:
    def __init__(self, filename, level='INFO'):
        self.level = self._get_level(level)
        self.filename = filename
        self.format = '%(asctime)s - %(levelname)s - %(message)s'
        self.console = Console()

    def _get_level(self, level):
        levels = {
            'DEBUG': 1,
            'INFO': 2,
            'WARNING': 3,
            'ERROR': 4,
            'CRITICAL': 5
        }
        return levels.get(level.upper(), 2)

    def log(self, level, message):
        if self._get_level(level) >= self.level:
            now = datetime.datetime.now()
            formatted = self.format.replace(
                '%(asctime)s', now.strftime('%Y-%m-%d %H:%M:%S'))
            formatted = formatted.replace('%(levelname)s', level.upper())
            formatted = formatted.replace('%(message)s', message)
            with open(self.filename, 'a') as f:
                f.write(formatted + '\n')
            style = ""
            match level:
                case 'DEBUG':
                    style = "bold blue"
                case 'INFO':
                    style = "bold green"
                case 'WARNING':
                    style = "bold yellow"
                case 'ERROR':
                    style = "bold white"
                case 'CRITICAL':
                    style = "bold red"
            self.console.print(formatted, style=style)

    def debug(self, message):
        self.log('DEBUG', message)

    def info(self, message):
        self.log('INFO', message)

    def warning(self, message):
        self.log('WARNING', message)

    def error(self, message):
        self.log('ERROR', message)

    def critical(self, message):
        self.log('CRITICAL', message)


server_logger = Logger('log/server.log', 'INFO')
