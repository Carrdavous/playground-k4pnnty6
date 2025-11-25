from skeleton import est_divisible_par_3
    

def test_est_divisible_par_3():
    try:
        test1 = est_divisible_par_3(17)
        assert test1 == False, f"17 est pas divisble par 3: {test1}... Attendu: True"
        test2 = est_divisible_par_3(39)
        assert test2 == True, "39 est divisible par 39: {test2}... Attentu: True"
        success()

        send_msg("Félicitations !", "Vous avez répondu correctement à l'énoncé")
    except AssertionError as e:
        fail()
        send_msg("Oups! 🐞", e)

if __name__ == "__main__":
    test_est_divisible_par_3()
