    TOKEN = Config.TOKEN
    WORKERS = Config.WORKERS
    TMDBAPI = Config.TMDBAPI
    DB_URI = Config.DB_URI
    GENIUS = Config.GENIUS
    SPT_CLIENT_SECRET = Config.SPT_CLIENT_SECRET
    SPT_CLIENT_ID = Config.SPT_CLIENT_ID
    DEBUG = Config.DEBUG
    ARLTOKEN = Config.ARL
    APP_URL = Config.APP_URL
    APIID = Config.APIID
    APIHASH = Config.APIHASH


if DEBUG:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )
else:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

__version__ = "1.1.3-rev09"

DEV_ID = 1329457821
LOG = logging.getLogger(__name__)

# Check python version:
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOG.info("You MUST need to have python version 3.6! shutting down...")
    sys.exit(1)


def typing(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.TYPING
        )
        return func(update, context, *args, **kwargs)

    return command_func


# Use HTML treewide;
defaults = Defaults(parse_mode=ParseMode.HTML)
updater = Updater(TOKEN, use_context=True, workers=WORKERS, defaults=defaults)
dp = updater.dispatcher
