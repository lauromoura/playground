#!/usr/bin/env elixir

defmodule Monty do

  @doors [:monster, :monster, :prize]

  def random_select do
    :random.uniform(3) - 1
  end

  def update_door(:keep, selected) do
    selected
  end

  def update_door(:change, 0), do: 2 # Open monster at #1
  def update_door(:change, 1), do: 2 # Open monster at #0
  def update_door(:change, 2), do: 1 # Open monster at #0

  def monty(decision) do
    selected_door = random_select()
    Enum.at @doors, update_door(decision, selected_door)
  end

  def seed_random do
    :random.seed(:erlang.phash2([node()]),
                  :erlang.monotonic_time(),
                  :erlang.unique_integer())
  end

  def main([]), do: main(["100"])
  def main(args) do
    seed_random
    iterations = String.to_integer(hd(args))
    range = 1..iterations
    won? = &(&1 == :prize)
    keep_wins = Stream.repeatedly(fn -> monty(:keep) end) |> Enum.take(iterations) |> Enum.count(won?)
    change_wins = Stream.repeatedly(fn -> monty(:change) end) |> Enum.take(iterations) |> Enum.count(won?)
    IO.puts ("Keeping choice won #{keep_wins} out of #{iterations} times")
    IO.puts ("Changing choice won #{change_wins} out of #{iterations} times")
  end
end

Monty.main(System.argv)
