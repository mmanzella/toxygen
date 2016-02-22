TOX_USER_STATUS = {
    'TOX_USER_STATUS_NONE': 0,
    'TOX_USER_STATUS_AWAY': 1,
    'TOX_USER_STATUS_BUSY': 2,
}

TOX_MESSAGE_TYPE = {
    'TOX_MESSAGE_TYPE_NORMAL': 0,
    'TOX_MESSAGE_TYPE_ACTION': 1,
}

TOX_PROXY_TYPE = {
    'TOX_PROXY_TYPE_NONE': 0,
    'TOX_PROXY_TYPE_HTTP': 1,
    'TOX_PROXY_TYPE_SOCKS5': 2,
}

TOX_SAVEDATA_TYPE = {
    'TOX_SAVEDATA_TYPE_NONE': 0,
    'TOX_SAVEDATA_TYPE_TOX_SAVE': 1,
    'TOX_SAVEDATA_TYPE_SECRET_KEY': 2,
}

TOX_ERR_OPTIONS_NEW = {
    'TOX_ERR_OPTIONS_NEW_OK': 0,
    'TOX_ERR_OPTIONS_NEW_MALLOC': 1,
}

TOX_ERR_NEW = {
    'TOX_ERR_NEW_OK': 0,
    'TOX_ERR_NEW_NULL': 1,
    'TOX_ERR_NEW_MALLOC': 2,
    'TOX_ERR_NEW_PORT_ALLOC': 3,
    'TOX_ERR_NEW_PROXY_BAD_TYPE': 4,
    'TOX_ERR_NEW_PROXY_BAD_HOST': 5,
    'TOX_ERR_NEW_PROXY_BAD_PORT': 6,
    'TOX_ERR_NEW_PROXY_NOT_FOUND': 7,
    'TOX_ERR_NEW_LOAD_ENCRYPTED': 8,
    'TOX_ERR_NEW_LOAD_BAD_FORMAT': 9,
}

TOX_ERR_BOOTSTRAP = {
    'TOX_ERR_BOOTSTRAP_OK': 0,
    'TOX_ERR_BOOTSTRAP_NULL': 1,
    'TOX_ERR_BOOTSTRAP_BAD_HOST': 2,
    'TOX_ERR_BOOTSTRAP_BAD_PORT': 3,
}

TOX_CONNECTION = {
    'TOX_CONNECTION_NONE': 0,
    'TOX_CONNECTION_TCP': 1,
    'TOX_CONNECTION_UDP': 2,
}

TOX_ERR_SET_INFO = {
    'TOX_ERR_SET_INFO_OK': 0,
    'TOX_ERR_SET_INFO_NULL': 1,
    'TOX_ERR_SET_INFO_TOO_LONG': 2,
}

TOX_ERR_FRIEND_ADD = {
    'TOX_ERR_FRIEND_ADD_OK': 0,
    'TOX_ERR_FRIEND_ADD_NULL': 1,
    'TOX_ERR_FRIEND_ADD_TOO_LONG': 2,
    'TOX_ERR_FRIEND_ADD_NO_MESSAGE': 3,
    'TOX_ERR_FRIEND_ADD_OWN_KEY': 4,
    'TOX_ERR_FRIEND_ADD_ALREADY_SENT': 5,
    'TOX_ERR_FRIEND_ADD_BAD_CHECKSUM': 6,
    'TOX_ERR_FRIEND_ADD_SET_NEW_NOSPAM': 7,
    'TOX_ERR_FRIEND_ADD_MALLOC': 8,
}

TOX_ERR_FRIEND_DELETE = {
    'TOX_ERR_FRIEND_DELETE_OK': 0,
    'TOX_ERR_FRIEND_DELETE_FRIEND_NOT_FOUND': 1,
}

TOX_ERR_FRIEND_BY_PUBLIC_KEY = {
    'TOX_ERR_FRIEND_BY_PUBLIC_KEY_OK': 0,
    'TOX_ERR_FRIEND_BY_PUBLIC_KEY_NULL': 1,
    'TOX_ERR_FRIEND_BY_PUBLIC_KEY_NOT_FOUND': 2,
}

TOX_ERR_FRIEND_GET_PUBLIC_KEY = {
    'OK': 0,
    'FRIEND_NOT_FOUND': 1,
}

TOX_ERR_FRIEND_GET_LAST_ONLINE = {
    'TOX_ERR_FRIEND_GET_LAST_ONLINE_OK': 0,
    'TOX_ERR_FRIEND_GET_LAST_ONLINE_FRIEND_NOT_FOUND': 1,
}

TOX_ERR_FRIEND_QUERY = {
    'TOX_ERR_FRIEND_QUERY_OK': 0,
    'TOX_ERR_FRIEND_QUERY_NULL': 1,
    'TOX_ERR_FRIEND_QUERY_FRIEND_NOT_FOUND': 2,
}

TOX_ERR_SET_TYPING = {
    'TOX_ERR_SET_TYPING_OK': 0,
    'TOX_ERR_SET_TYPING_FRIEND_NOT_FOUND': 1,
}

TOX_ERR_FRIEND_SEND_MESSAGE = {
    'OK': 0,
    'NULL': 1,
    'FRIEND_NOT_FOUND': 2,
    'FRIEND_NOT_CONNECTED': 3,
    'SENDQ': 4,
    'TOO_LONG': 5,
    'EMPTY': 6,
}

TOX_FILE_KIND = {
    'TOX_FILE_KIND_DATA': 0,
    'TOX_FILE_KIND_AVATAR': 1,
}

TOX_FILE_CONTROL = {
    'TOX_FILE_CONTROL_RESUME': 0,
    'TOX_FILE_CONTROL_PAUSE': 1,
    'TOX_FILE_CONTROL_CANCEL': 2,
}

TOX_ERR_FILE_CONTROL = {
    'TOX_ERR_FILE_CONTROL_OK': 0,
    'TOX_ERR_FILE_CONTROL_FRIEND_NOT_FOUND': 1,
    'TOX_ERR_FILE_CONTROL_FRIEND_NOT_CONNECTED': 2,
    'TOX_ERR_FILE_CONTROL_NOT_FOUND': 3,
    'TOX_ERR_FILE_CONTROL_NOT_PAUSED': 4,
    'TOX_ERR_FILE_CONTROL_DENIED': 5,
    'TOX_ERR_FILE_CONTROL_ALREADY_PAUSED': 6,
    'TOX_ERR_FILE_CONTROL_SENDQ': 7,
}

TOX_ERR_FILE_SEEK = {
    'TOX_ERR_FILE_SEEK_OK': 0,
    'TOX_ERR_FILE_SEEK_FRIEND_NOT_FOUND': 1,
    'TOX_ERR_FILE_SEEK_FRIEND_NOT_CONNECTED': 2,
    'TOX_ERR_FILE_SEEK_NOT_FOUND': 3,
    'TOX_ERR_FILE_SEEK_DENIED': 4,
    'TOX_ERR_FILE_SEEK_INVALID_POSITION': 5,
    'TOX_ERR_FILE_SEEK_SENDQ': 6,
}

TOX_ERR_FILE_GET = {
    'TOX_ERR_FILE_GET_OK': 0,
    'TOX_ERR_FILE_GET_NULL': 1,
    'TOX_ERR_FILE_GET_FRIEND_NOT_FOUND': 2,
    'TOX_ERR_FILE_GET_NOT_FOUND': 3,
}

TOX_ERR_FILE_SEND = {
    'TOX_ERR_FILE_SEND_OK': 0,
    'TOX_ERR_FILE_SEND_NULL': 1,
    'TOX_ERR_FILE_SEND_FRIEND_NOT_FOUND': 2,
    'TOX_ERR_FILE_SEND_FRIEND_NOT_CONNECTED': 3,
    'TOX_ERR_FILE_SEND_NAME_TOO_LONG': 4,
    'TOX_ERR_FILE_SEND_TOO_MANY': 5,
}

TOX_ERR_FILE_SEND_CHUNK = {
    'TOX_ERR_FILE_SEND_CHUNK_OK': 0,
    'TOX_ERR_FILE_SEND_CHUNK_NULL': 1,
    'TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_FOUND': 2,
    'TOX_ERR_FILE_SEND_CHUNK_FRIEND_NOT_CONNECTED': 3,
    'TOX_ERR_FILE_SEND_CHUNK_NOT_FOUND': 4,
    'TOX_ERR_FILE_SEND_CHUNK_NOT_TRANSFERRING': 5,
    'TOX_ERR_FILE_SEND_CHUNK_INVALID_LENGTH': 6,
    'TOX_ERR_FILE_SEND_CHUNK_SENDQ': 7,
    'TOX_ERR_FILE_SEND_CHUNK_WRONG_POSITION': 8,
}

TOX_ERR_FRIEND_CUSTOM_PACKET = {
    'TOX_ERR_FRIEND_CUSTOM_PACKET_OK': 0,
    'TOX_ERR_FRIEND_CUSTOM_PACKET_NULL': 1,
    'TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_FOUND': 2,
    'TOX_ERR_FRIEND_CUSTOM_PACKET_FRIEND_NOT_CONNECTED': 3,
    'TOX_ERR_FRIEND_CUSTOM_PACKET_INVALID': 4,
    'TOX_ERR_FRIEND_CUSTOM_PACKET_EMPTY': 5,
    'TOX_ERR_FRIEND_CUSTOM_PACKET_TOO_LONG': 6,
    'TOX_ERR_FRIEND_CUSTOM_PACKET_SENDQ': 7,
}

TOX_ERR_GET_PORT = {
    'TOX_ERR_GET_PORT_OK': 0,
    'TOX_ERR_GET_PORT_NOT_BOUND': 1,
}

TOX_PUBLIC_KEY_SIZE = 32

TOX_ADDRESS_SIZE = TOX_PUBLIC_KEY_SIZE + 48

TOX_MAX_FRIEND_REQUEST_LENGTH = 1016

TOX_MAX_MESSAGE_LENGTH = 1372

TOX_MAX_NAME_LENGTH = 128

TOX_MAX_STATUS_MESSAGE_LENGTH = 1007
