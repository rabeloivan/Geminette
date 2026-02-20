/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ex08_harness.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rabeloivan <rabeloivan@student.42.fr>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/19 16:27:32 by rabeloivan        #+#    #+#             */
/*   Updated: 2026/02/19 22:54:07 by rabeloivan       ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_sort_int_tab(int *tab, int size);

int	main(void)
{
	int	size;
	int	tab[1000];
	int	i;

	if (scanf("%d", &size) == 1 && size >= 0 && size <= 1000)
	{
		i = 0;
		while (i < size)
		{
			scanf("%d", &tab[i]);
			i++;
		}
		ft_sort_int_tab(tab, size);
		i = 0;
		while (i < size)
		{
			printf("%d", tab[i]);
			if (i < size - 1)
				printf(" ");
				i++;
		}
	}
	return (0);
}
