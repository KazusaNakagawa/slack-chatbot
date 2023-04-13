# TimedRotatingFileHandler を使ってログを出力する
import logging
from logging.handlers import TimedRotatingFileHandler

# ログファイルの出力先
LOG_FILE = 'logger_time.log'


# ロガーの取得
logger = logging.getLogger(__name__)


def create_second_handler(when='S', interval=10, backup_count=3):
  """ ログファイルのハンドラを作成

  Arguments:
    when {str} -- ローテーションの単位 (default: {'S'})
    interval {int} -- ローテーションの間隔 (default: {10})
    backup_count {int} -- バックアップファイルの数 (default: {3})

  Returns:
    [type] -- [description]
  """
  handler = TimedRotatingFileHandler(
      LOG_FILE,
      when=when,
      interval=interval,  
      backupCount=backup_count,
      )
  return handler

def set_handler(handler):
  # ログレベルの設定
  logging.basicConfig(
      level=logging.DEBUG,  
      format='%(asctime)s %(levelname)s %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S',
      handlers=[handler],
      )


def main():
  # ログファイルのハンドラを作成
  handler = create_second_handler()
  # ログファイルのハンドラを設定
  set_handler(handler)
  # ログを出力
  logger.debug('debug message')
  logger.info('info message')
  logger.warning('warning message')
  logger.error('error message')
  logger.critical('critical message')

# 生成したログファイルを圧縮する (gzip)
# import gzip

# with open(LOG_FILE, 'rb') as f_in:
#     with gzip.open(LOG_FILE + '.gz', 'wb') as f_out:
#         f_out.writelines(f_in)

# ログファイルを削除する
import os

# os.remove(LOG_FILE)

# ログファイルを解凍する (gzip)
# import gzip

# with gzip.open(LOG_FILE + '.gz', 'rb') as f_in:
#     with open(LOG_FILE, 'wb') as f_out:
#         f_out.writelines(f_in)

# ログファイルを表示する
# with open(LOG_FILE, 'r') as f:
#     print(f.read())

def test_create_second_handler():
  """ ログファイルのハンドラを作成するテスト
  """
  handler = create_second_handler()
  assert isinstance(handler, TimedRotatingFileHandler)

def test_set_handler():
  """ ログファイルのハンドラを設定するテスト
  """
  handler = create_second_handler()
  set_handler(handler)
  assert logger.level == logging.DEBUG
  assert logger.handlers[0] == handler


def test_main():
  """ ログファイルを出力するテスト
  """
  main()
  assert os.path.exists(LOG_FILE)

if __name__ == '__main__':
  main()
