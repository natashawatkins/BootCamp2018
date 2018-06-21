from random import choice


def random_walk(max_iters=1e12):
    try:
        walk = 0
        directions = [1, -1]
        for i in range(int(max_iters)):
            walk += choice(directions)
        print("Process completed")
    except KeyboardInterrupt:
        print(f"Process interrupted at iteration {i}")
    finally:
        return walk