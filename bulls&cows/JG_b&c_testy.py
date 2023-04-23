import JG_bulls_and_cows
import pytest

dic = JG_bulls_and_cows.Dictionary()
val = JG_bulls_and_cows.Validator()
en = JG_bulls_and_cows.Engine()


# test czy funkcja losuje słowo o dobrej długości w zależności od poziomu trudności
@pytest.mark.parametrize("diff, x", [(1, [1, 2, 3, 4]), (2, [5, 6]), (3, [7, 8, 9, 10, 11, 12, 13, 14])])
def test_choose_word(diff, x):
    assert len(dic.choose_word(diff)) in x


# test czy funckja poprawnie rozpoznaje stringi izogramy
@pytest.mark.parametrize("word, x", [("pies", 1), (6, 0), (True, 0), ("kotek", 0), ("pchła", 1)])
def test_check_word(word, x):
    assert val.check_word(word) == x


# test czy funckja poprawnie zmienia liczbę prób w silniku
@pytest.mark.parametrize("att1, att2", [(2, (2, 2)), (3, (3, 3)), (6, (6, 6)), (20, (20, 20))])
def test_change_attempts(att1, att2):
    assert en.change_attempts(att1) == att2


# test czy funkcja niezależnie, dla każdego przypadku dobrze oblicza liczby bulls i cows
@pytest.mark.parametrize("user, word, b, c", [("pies", "kot", 0, 0), ("pies", "donica", 0, 1), ("kot", "kura", 1, 0)])
def test_bull_cow_count(user, word, b, c):
    assert en.bull_cow_count(user, word) == (b, c)


# test czy funkcja rozpoznaje wygrana (zwraca wtedy 0)
@pytest.mark.parametrize("bulls, word1, y", [(2, "kot", 0), (4, "pies", 1), (5, "kura", 0)])
def test_win(bulls, word1, y):
    assert en.win(bulls, word1) == y


# test czy funkcja po kazdej próbie zmniejsza liczbę prób o 1 i zeruje bulls i cows
@pytest.mark.parametrize("at, bu, co, at1, bu1, co1", [(1, 2, 3, 0, 0, 0), (2, 5, 3, 1, 0, 0), (5, 4, 3, 4, 0, 0)])
def test_stats(at, bu, co, at1, bu1, co1):
    assert en.stats(at, bu, co) == (at1, bu1, co1)


# test czy funkcja poprawnie zapisuje izogramy do bazy
@pytest.mark.parametrize("word", ["miś", "piłka"])
def test_add_word_good(word):
    assert en.add_word(word) in en.dict.data


# test czy funkcja nie zapisuje słów niebędące izogramami
@pytest.mark.parametrize("word", ["kotek", "małpa"])
def test_add_word_bad(word):
    assert en.add_word(word) not in en.dict.data
