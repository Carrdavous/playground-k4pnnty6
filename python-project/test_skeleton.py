from skeleton import est_divisible_par_3
    

def test_est_divisible_par_3():
    try:
        test1 = est_divisible_par_3(17)
        assert test1 == False, f"17 est pas divisble par 3: {test1}... Attendu: True"
        test2 = est_divisible_par_3(39)
        assert test2 == True, "39 est divisible par 39: {test2}... Attentu: True"
        success()

        if sum_builtin_used:
            send_msg("My personal Yoda, you are. 🙏", "* ● ¸ .　¸. :° ☾ ° 　¸. ● ¸ .　　¸.　:. • ")
            send_msg("My personal Yoda, you are. 🙏", "           　★ °  ☆ ¸. ¸ 　★　 :.　 .   ")
            send_msg("My personal Yoda, you are. 🙏", "__.-._     ° . .　　　　.　☾ ° 　. *   ¸ .")
            send_msg("My personal Yoda, you are. 🙏", "'-._\\7'      .　　° ☾  ° 　¸.☆  ● .　　　")
            send_msg("My personal Yoda, you are. 🙏", " /'.-c    　   * ●  ¸.　　°     ° 　¸.    ")
            send_msg("My personal Yoda, you are. 🙏", " |  /T      　　°     ° 　¸.     ¸ .　　  ")
            send_msg("My personal Yoda, you are. 🙏", "_)_/LI")
        else:
            send_msg("Kudos 🌟", "Did you know that you could use the sum function? Try it!")
            send_msg("Kudos 🌟", "")
            send_msg("Kudos 🌟", "galaxies = [37, 3, 2]")
            send_msg("Kudos 🌟", "total_stars = sum(galaxies)  # 42")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")


if __name__ == "__main__":
    test_something()
