from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.tennis_p = TennisPlayer('name', 20, 0.0)

    def test__init__(self):
        assert 'name' == self.tennis_p.name
        assert 20 == self.tennis_p.age
        assert 0.0 == self.tennis_p.points
        assert isinstance(self.tennis_p.points, float)
        assert [] == self.tennis_p.wins
        assert isinstance(self.tennis_p.wins, list)

    def test_name_setter_wrong_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.tennis_p.name = 'na'

        expected = "Name should be more than 2 symbols!"
        self.assertEqual(expected, str(ex.exception))

    def test_age_setter_wrong_age_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.tennis_p.age = 10

        expected = "Players must be at least 18 years of age!"
        self.assertEqual(expected, str(ex.exception))

    def test_trying_to_initialize_with_wrong_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer('na', 22, 0.0)

        expected = "Name should be more than 2 symbols!"
        self.assertEqual(expected, str(ex.exception))

    def test_trying_to_initialize_with_wrong_age_raises(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer('name', 5, 0.0)

        expected = "Players must be at least 18 years of age!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_new_win_method_tournament_not_in_win_adds_name(self):
        self.assertEqual([], self.tennis_p.wins)
        self.tennis_p.add_new_win('tour')
        self.assertEqual(['tour'], self.tennis_p.wins)
        self.tennis_p.add_new_win('tour_2')
        self.assertEqual(['tour', 'tour_2'], self.tennis_p.wins)

    def test_add_new_win_method_tournament_already_in_list_returns_message(self):
        self.assertEqual([], self.tennis_p.wins)
        self.tennis_p.add_new_win('tour')
        expected = "tour has been already added to the list of wins!"
        result = self.tennis_p.add_new_win('tour')
        self.assertEqual(expected, result)

    def test__less_than__overridden_correctly(self):
        other = TennisPlayer('name2', 22, 2.2)
        expected = "name2 is a top seeded player and he/she is better than name"
        result = self.tennis_p < other
        self.assertEqual(expected, result)

    def test__less_than__overridden_correctly_2(self):
        other = TennisPlayer('name2', 22, 2.2)
        expected = "name2 is a better player than name"
        result = self.tennis_p > other
        self.assertEqual(expected, result)

    def test__str__method_returns_correct_message(self):
        self.tennis_p.add_new_win('tournament')
        self.tennis_p.add_new_win('tournament2')
        expected = "Tennis Player: name\nAge: 20\nPoints: 0.0\nTournaments won: tournament, tournament2"
        result = str(self.tennis_p)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()