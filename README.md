# discgolf
New version of my game inspired by Zork and Planetfall, but much better organized this time
# 📝 Disc Golf CLI Game – TODO

## 🚨 Critical Fixes (Do These First)

* [ ] **Add end-of-round handling**

  * Prevent crash after Hole 9
  * Example:

    ```python
    if current_hole > 9:
        print("Round complete!")
        break
    ```

* [ ] **Handle invalid input safely**

  * Right now `(None, None)` still gets processed
  * Add guard:

    ```python
    if throw_type is None:
        print("Invalid input")
        continue
    ```

---

## 🎯 Gameplay Improvements

* [ ] **Force putting in circle**

  * Ignore user input when in `"circle1"` or `"circle2"`
  * Automatically set:

    ```python
    throw_type = "putt"
    disc_type = "putter"
    ```

* [ ] **Improve missed putt realism**

  * Current:

    ```python
    random.uniform(0.1, 1.0)
    ```
  * Change to allow overshooting:

    ```python
    random.uniform(0.5, 1.3)
    ```

* [ ] **Add “tap-in” logic**

  * If `current_distance <= 3`, auto-make putt

* [ ] **Prevent unrealistic throws in circle**

  * Option 1: block them
  * Option 2: heavily penalize accuracy

---

## 📊 Scoring & Feedback

* [ ] **Display strokes per hole after completion**

  * Example:

    ```
    Hole 3 complete in 4 strokes (+1)
    ```

* [ ] **Show score relative to par**

  * Convert score to:

    * Birdie (-1)
    * Par (0)
    * Bogey (+1), etc.

* [ ] **Display running total more clearly**

  * Example:

    ```
    Total Score: -2 (through 4 holes)
    ```

---

## 🧠 Code Structure / Cleanup

* [ ] **Remove repetitive shot logic**

  * You duplicate shot handling in 2 places
  * Extract into a helper function:

    ```python
    def handle_shot(...):
        pass
    ```

* [ ] **Simplify hole system**

  * Replace 9 classes with a list:

    ```python
    holes = [
        {"length": 412, "par": 3},
        {"length": 251, "par": 3},
        {"length": 512, "par": 4},
        {"length": 310, "par": 3},
        {"length": 950, "par": 5},
        {"length": 230, "par": 3},
        {"length": 750, "par": 4},
        {"length": 460, "par": 4},
        {"length": 1000, "par": 5},
    ]
    ```

* [ ] **Remove unused imports**

  * `os`, `re` aren’t used

* [ ] **Remove or implement `odd_choice`**

  * Either:

    * Make it affect gameplay
    * Or delete it

---

## 🎮 User Experience

* [ ] **Improve `output_results()`**

  * Show cleaner, game-like messages:

    * “Great shot! You're in Circle 1 (25 ft)”
    * “Missed putt, 12 ft comeback”

* [ ] **Add input help**

  * If invalid input:

    ```
    Try: 'backhand driver' or 'forehand midrange'
    ```

* [ ] **Allow simple inputs**

  * Accept:

    * `"bh driver"`
    * `"fh mid"`
    * `"putt"`

---

## 🌪️ Optional Features (Fun Additions)

* [ ] **Wind system**

  * Random modifier to accuracy/distance

* [ ] **Disc selection strategy**

  * Suggest optimal disc based on distance

* [ ] **Hazards**

  * Add penalty strokes for bad misses

* [ ] **Scorecard at end**

  * Show all holes + strokes

---

## 🧪 Balancing / Tuning

* [ ] **Adjust accuracy values**

  * Drivers might be too forgiving/unforgiving

* [ ] **Tune rough penalties**

  * Current:

    * `-20`, `-30`
  * Test for feel

* [ ] **Tune putting percentages**

  * Circle 1 at 89% is very generous

---

## 🧹 Nice-to-Have Polish

* [ ] **Clear screen between shots**
* [ ] **Add separators between turns**
* [ ] **Add “Press Enter to continue” between holes**

---

## 🏁 Stretch Goal

* [ ] **Refactor into classes**

  * `Game`
  * `Hole`
  * `Player`

