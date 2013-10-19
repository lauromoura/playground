-module (euler).

-export ([problem1/0,problem2/0]).

% Get the list of mutiples for a number until
problem1() ->
    lists:sum([X || X <- lists:seq(1,1000-1),
            (X rem 3 =:= 0) or (X rem 5 =:= 0)]).

% Ugly!!!!!
fibonacciSequenceTail(Top, []) ->
    if Top =< 2 ->
        [1];
       Top > 2 ->
        fibonacciSequenceTail(Top, [2,1])
    end;
fibonacciSequenceTail(Top, Acc=[H1| [H2| Tail]]) ->
    if Top =< H1 ->
        [H2 | Tail];
       Top > H1 ->
        fibonacciSequenceTail(Top, [H1+H2 | Acc])
    end.

% Sequence of fibonacci numbers up to Top.
fibonacciSequence(Top) ->
    fibonacciSequenceTail(Top, []).

problem2() ->
    lists:sum([X || X <- fibonacciSequence(4000000), X rem 2 =:= 0]).
