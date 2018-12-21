# For Patient model.
# Sex
MALE = 'male'
FEMALE = 'female'
SEX = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
)

# Race
AMERICAN_INDIAN = 'american indian'
ALASKA_NATIVE = 'alaska native'
WHITE = 'white'
BLACK_OR_AFRICAN_AMERICAN = 'black or african american'
NATIVE_HAWAIIAN = 'native hawaiian'
PACIFIC_ISLANDER = 'pacific islander'
HISPANIC = 'hispanic'
TWO_OR_MORE_RACES = 'two or more races'
ASIAN = 'asian'
RACE = (
    (AMERICAN_INDIAN, 'American Indian'),
    (ALASKA_NATIVE, 'Alaska Native'),
    (ASIAN, 'Asian'),
    (WHITE, 'White'),
    (BLACK_OR_AFRICAN_AMERICAN, 'Black or African American'),
    (NATIVE_HAWAIIAN, 'Native Hawaiian'),
    (PACIFIC_ISLANDER, 'Pacific Islander'),
    (HISPANIC, 'Hispanic'),
    (TWO_OR_MORE_RACES, 'Two or more races'),
)

# For HealthEncounter model.
# Type of health encounter
SURGERY = 'surgery'
ROUTINE_PHYSICAL = 'routine physical'
GENERAL_ILLNESS = 'general illness'
EMERGENCY_ROOM = 'emergency room'
TYPE_OF_HEALTH_ENCOUNTER = (
    (SURGERY, 'Surgery'),
    (ROUTINE_PHYSICAL, 'Routine Physical'),
    (GENERAL_ILLNESS, 'General Illness'),
    (EMERGENCY_ROOM, 'Emergency Room'),
)



