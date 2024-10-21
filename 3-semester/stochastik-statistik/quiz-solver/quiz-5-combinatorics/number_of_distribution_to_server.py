from math import comb

def number_of_distribution_to_server(number_of_servers, number_of_copies):
    """
    This function returns the number of ways you can distribute n copies of a backup to x servers.
    It is also possible to have no or all copies on a server.

    :param int number_of_servers: number of servers
    :param int number_of_copies: number of copies
    :return: number of ways you can distribute the copies
    :rtype: int
    """

    return comb(number_of_servers + number_of_copies - 1, number_of_copies)