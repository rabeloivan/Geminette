/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ex05_harness.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rabeloivan <rabeloivan@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/19 16:28:40 by rabeloivan        #+#    #+#             */
/*   Updated: 2026/02/19 16:28:41 by rabeloivan       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putstr(char *str);

int	main(void)
{
	char	buffer[2048];
	int		bytes_read;

	bytes_read = read(0, buffer, 2047);
	if (bytes_read > 0)
	{
		buffer[bytes_read] = '\0';
		ft_putstr(buffer);
	}
	return (0);
}
