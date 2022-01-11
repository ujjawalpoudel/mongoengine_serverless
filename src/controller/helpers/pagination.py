def skiplimit(page_size, page_num):
    """Calculate offset and limit for pagination

    Args:
        page_size (int): total number of rows per page
        page_num (int): page number

    Returns:
        offset (int): skip that many rows before beginning to return rows
        limit (int): items per page
    """
    offset = page_size * (page_num - 1)
    limit = page_size
    return offset, limit
