
import time

def guess_the_riddle():
    riddles = {
        "من همیشه در حال حرکت هستم اما هرگز جایی نمی‌روم. چه چیزی هستم؟": "زمان",
        "چیزی که اگر آن را به من بدهید، آن را از دست می‌دهید. چه چیزی هستم؟": "راز",
        "چند کلاغ بر روی درخت نشسته‌اند و دو تا از آنها پرواز می‌کنند، چندتا باقی می‌ماند؟": "دو",
    }

    score = 0
    print("به بازی معما خوش آمدید!")
    print("شما 10 ثانیه زمان دارید تا به هر معما پاسخ دهید.")
    
    for riddle, answer in riddles.items():
        print("\nمعما: ", riddle)
        start_time = time.time()
        
        player_answer = input("پاسخ شما: ").strip()

        elapsed_time = time.time() - start_time

        if elapsed_time > 10:
            print("زمان شما تمام شد!")
            print(f"پاسخ درست: {answer}")
            continue

        if player_answer == answer:
            print("تبریک! پاسخ درست است.")
            score += 1
        else:
            print(f"پاسخ درست: {answer}")

    print(f"\nبازی تمام شد. امتیاز شما: {score}")

guess_the_riddle()