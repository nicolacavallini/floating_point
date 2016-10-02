#include <stdio.h>

int main()
{
    int i;
    float delta_t = .1;
    float time = 0;

    float missle_speed = 2000;
    float spatial_precision;

    float miss_match;

    int num_steps = 2e+5;

    float simulated_time = ((float)num_steps+1)*delta_t/3600;

    for (i = 0; i< num_steps; i++)
    {
        time = time + delta_t;
        miss_match = time - ((float)i+1.)*delta_t;

        spatial_precision = miss_match*missle_speed;

    }

    printf("elapsed time %e\n",simulated_time);

    printf("spatial precision %e meters\n",spatial_precision);
    return 0;
}
