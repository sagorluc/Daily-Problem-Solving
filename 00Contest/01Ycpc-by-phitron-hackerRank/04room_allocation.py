# Problem link: https://www.hackerrank.com/contests/ycpc-by-phitron-1st-round-beginner-level-contest-1-2024-1/challenges/room-allocation-3-3

def collect_inputs():
    T = int(input('Enter number of test cases: ').strip())
    test_cases = []
    
    for _ in range(T):
        inputs_rooms_students = input('Enter number of rooms and students: ').strip().split()
        input_room = int(inputs_rooms_students[0])
        input_student = int(inputs_rooms_students[1])
        
        students = []
        for _ in range(input_student):
            inputs_all = input('Enter roll, name, room, gender: ').strip().split()
            roll = int(inputs_all[0])
            name = inputs_all[1]
            room = int(inputs_all[2])
            gender = inputs_all[3]
            students.append({
                'roll': roll,
                'name': name,
                'room': room,
                'gender': gender
            })
        
        allocate_room = []
        query = int(input('Enter query>> '))
        for _ in range(query):    
            input_allo_room = list(map(int, input('Enter allocated room: ').strip().split()))
            allocate_room.append(input_allo_room)
        
        test_cases.append({
            'rooms_students': (input_room, input_student),
            'students': students,
            'allocate_room': allocate_room,
            'query': query,
        })

    return test_cases


def process_test_cases(test_cases):
    for case_index, case in enumerate(test_cases):
        print(f"Case #{case_index + 1}:")
        query = case['query']
        students = case['students']

        # Allocate students to their respective rooms in the query
        room_allocation = {}
        for student in students:
            room_number = student['room']
            if room_number not in room_allocation:
                room_allocation[room_number] = []
            room_allocation[room_number].append(student)

        # Sort room numbers
        sorted_rooms = sorted(room_allocation.keys())

        # Print the results for each query
        for query_index, room in enumerate(sorted_rooms):
            print(f"Query #{query_index + 1}:")
            # Sort students by roll number within the room
            sorted_students = sorted(room_allocation[room], key=lambda x: x['roll'])
            for student in sorted_students:
                print(f"{student['roll']} {student['name']} {student['gender']}")
        print()



def main():
    test_cases = collect_inputs()
    process_test_cases(test_cases)


if __name__ == "__main__":
    main()






# T = int(input('Enter test case>> '))
# Q = 1
# alocate_room = []
# all_student = []
# for ts in range(T):
#     inputs_rooms_students = input('Enter Rooms and Students>> ').split()
#     input_room = inputs_rooms_students[0]
#     input_student = inputs_rooms_students[1]
#     input_room = int(input_room)
#     input_student = int(input_student)
    
#     for st in range(input_student):
#         inputs_all = input('Enter roll, name, room, gender>> ').split()
#         all_student.append(inputs_all)
#         input_roll = inputs_all[0]
#         input_name = inputs_all[1]
#         input_room = inputs_all[2]
#         input_gender = inputs_all[3]
        
#         input_roll = int(input_roll)
#         input_room = int(input_room)
        
#     for alo_room in range(input_student):    
#         input_allo_room = list(map(int, input('Enter allocate romm>> ').split()))
#         alocate_room.append(input_allo_room)
        
    
#     roll_room = {}
    
#     for i in range(len(inputs_all)):
#         for st[i] in inputs_all:
#             roll_number = st[i[0]]
    
#     print(ts+1, 'test case')
#     print(alocate_room, 'alocate room')
#     print(inputs_rooms_students, 'inputs_rooms_students')
#     print(sorted(inputs_all.roll), 'inputs_all')
    
    