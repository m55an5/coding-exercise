from coding_exercise.domain.model.cable import Cable

class Splitter:
    MIN_CABLE_LENGTH=2
    MAX_CABLE_LENGTH=1024
    MIN_TIMES_VALUE=1
    MAX_TIMES_VALUE=64

    def __validate(self, cable_length, times):
        if not (self.MIN_CABLE_LENGTH <= cable_length <= self.MAX_CABLE_LENGTH):
            raise ValueError(f"Cable length must be between {self.MIN_CABLE_LENGTH} and {self.MAX_CABLE_LENGTH}")
        if not (self.MIN_TIMES_VALUE <= times <= self.MAX_TIMES_VALUE):
            raise ValueError(f"Times value must be between {self.MIN_TIMES_VALUE} and {self.MAX_TIMES_VALUE}")

    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.__validate(cable.length, times)

        sub_cables = []

        # find the maximum lenth that can be achieved w.r.t. n (times)
        max_length = cable.length // (times + 1)

        if max_length < 1:
            raise ValueError

        # total cables possible with max length (quotient)
        max_sub_cables = cable.length // max_length
        
        for n in range(max_sub_cables):
            c = Cable(max_length, self.format_cable_name(cable.name, sub_cables))
            sub_cables.append(c)
        
        # find quotient which gives remaing length of original cable
        remaining_cable_length = cable.length % max_length

        while remaining_cable_length >= max_length:
            c = Cable(max_length, self.format_cable_name(cable.name, sub_cables))
            remaining_cable_length -= max_length
            sub_cables.append(c)

        # if there is still some length of cable left or the reaiming cable is less than
        # max length calculated earlier 
        if remaining_cable_length > 0:
            c = Cable(remaining_cable_length, self.format_cable_name(cable.name, sub_cables))
            sub_cables.append(c)

        return sub_cables

    def format_cable_name(self, name, list):
        return f"{name}-{len(list):02}"
