# discgolf
New version of my game inspired by Zork and Planetfall, but much better organized this time
# Text-Based Disc Golf Game – TODO

## Critical Fixes (Do These First)

* **Add end-of-round handling**

  * Prevent crash after Hole 9
  * Example:

    ```python
    if current_hole > 9:
        print("Round complete!")
        break
    ```

  * **Handle invalid input safely**

  * Right now `(None, None)` still gets processed
  * Add guard:

    ```python
    if throw_type is None:
        print("Invalid input")
        continue
    ```

---

## Gameplay Improvements

* **Add “tap-in” logic**

  * If `current_distance <= 3`, auto-make putt

---

*  **Add input help**

  * If invalid input:

    ```
    Try: 'backhand driver' or 'forehand midrange'
    ```

*  **Allow simple inputs**

  * Accept:

    * `"bh driver"`
    * `"fh mid"`
    * `"putt"`

---

## Optional Feature

*  **Scorecard at end**

  * Show all holes + strokes

---

## Nice-to-Have Polish

* [ ] **Clear screen between shots**
* [ ] **Add separators between turns**
* [ ] **Add “Press Enter to continue” between holes**


