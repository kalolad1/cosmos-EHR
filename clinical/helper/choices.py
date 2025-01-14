# For Patient model.
# Sex.
MALE = 'male'
FEMALE = 'female'
SEX = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
)

# Race.
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


# For the Relative model.
# Type of relationship.
BROTHER = 'brother'
SISTER = 'sister'
FATHER = 'father'
MOTHER = 'mother'
GRANDFATHER_PATERNAL = 'grandfather paternal'
GRANDMOTHER_PATERNAL = 'grandmother paternal'
GRANDFATHER_MATERNAL = 'grandfather maternal'
GRANDMOTHER_MATERNAL = 'grandmother maternal'
RELATIONSHIP = (
    (BROTHER, 'Brother'),
    (SISTER, 'Sister'),
    (FATHER, 'Father'),
    (MOTHER, 'Mother'),
    (GRANDFATHER_PATERNAL, 'Grandfather Paternal'),
    (GRANDMOTHER_PATERNAL, 'Grandmother Paternal'),
    (GRANDFATHER_MATERNAL, 'Grandfather Maternal'),
    (GRANDMOTHER_MATERNAL, 'Grandmother Maternal'),
)


# For HealthEncounter model.
# Type of health encounter.
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

# Dictionary of health encounter types mapped to their Font Awesome icons (used in the
# timeline of the patient story).
HE_TO_ICON = {
    SURGERY: 'fa fa-bed',
    ROUTINE_PHYSICAL: 'fa fa-calendar-check-o',
    GENERAL_ILLNESS: '	fa fa-thermometer-4',
    EMERGENCY_ROOM: 'fa fa-flash',
}





