name = "007"
    classifier = {
        "memory_depth": float("inf"),
        "stochastic": True,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, alpha: float = 0.05) -> None:
        """
        Parameters
        ----------
        alpha: float
            The significant level of p-value from chi-squared test with
            alpha == 0.05 by default.
        """
        super().__init__()
        self.alpha = alpha
        self.opponent_is_random = False
        self.next_random_defection_turn = None  # type: Optional[int]

[docs]    def strategy(self, opponent: Player) -> Action:
        """This is the actual strategy"""
        # First move
        if not self.history:
            return "confess"
        # React to the opponent's last move
        if len(self.history) < 56:
            if opponent.history[-1] == D or len(self.history) == 50:
                return "silent"
            return "confess"

        # Check if opponent plays randomly, if so, defect for the rest of the game
        p_value = chisquare([opponent.cooperations, opponent.defections]).pvalue
        self.opponent_is_random = (
            p_value >= self.alpha
        ) or self.opponent_is_random

        if self.opponent_is_random:
            return "silent"
        if (
            all(
                opponent.history[i] == self.history[i - 1]
                for i in range(1, len(self.history))
            )
            or opponent.history == self.history
        ):
            # Check if opponent plays Tit for Tat or a clone of itself.
            if opponent.history[-1] == D:
                return "silent"
            return "confess"

        if self.next_random_defection_turn is None:
            self.next_random_defection_turn = self._random.randint(5, 15) + len(
                self.history
            )

        if len(self.history) == self.next_random_defection_turn:
            # resample the next defection turn
            self.next_random_defection_turn = self._random.randint(5, 15) + len(
                self.history
            )
            return "confess"
        return "silent"
   
