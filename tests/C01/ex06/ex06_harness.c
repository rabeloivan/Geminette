/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ex06_harness.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rabeloivan <rabeloivan@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/19 16:28:36 by rabeloivan        #+#    #+#             */
/*   Updated: 2026/02/19 16:28:37 by rabeloivan       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>

int	ft_strlen(char *str);

int	main(void)
{
	char	buffer[2048];
	int		bytes_read;

	bytes_read = read(0, buffer, 2047);
	if (bytes_read >= 0)
	{
		buffer[bytes_read] = '\0';
		printf("%d", ft_strlen(buffer));
	}
	return (0);
}
