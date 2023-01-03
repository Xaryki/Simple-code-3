class schedule:
    @classmethod
    def day_schedule(cls, day: str, schedule: list):
        schedule_for_whole_day = '\033[1m' + str(day) + '\033[0m' + ":\n"
        schedule_time = schedule[0]
        schedule_subjects = schedule[1]
        for i in range(len(schedule_time)):
            schedule_for_whole_day += "  " + '\x1B[3m' + '\033[1m' + '\033[4m' + schedule_time[
                i] + '\x1B[0m' + '\033[0m' + '\n'
            schedule_for_whole_day += "  " + '\033[1m' + "|" + schedule_subjects[i] + '\033[0m' + '\n\n'
        return schedule_for_whole_day

    @classmethod
    def week_schedule(cls, schedule : dict):
        schedule_for_whole_week = ""
        for day in schedule:
            schedule_for_whole_week += cls.day_schedule(day, schedule[day])
        return schedule_for_whole_week


