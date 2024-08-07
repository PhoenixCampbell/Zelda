# game setup
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = "./graphics/font/joystix.ttf"
UI_FONT_SIZE = 18

# gen colours
WATER_COLOUR = "#71ddee"
UI_BG_COLOUR = "#222222"
UI_BORDER_COLOUR = "#111111"
TEXT_COLOUR = "#EEEEEE"

# ui colours
HEALTH_COLOUR = "red"
ENERGY_COLOUR = "blue"
UI_BORDER_COLOUR_ACTIVE = "gold"

weaponData = {
    "sword": {
        "cooldown": 100,
        "damage": 15,
        "graphic": "./graphics/weapons/sword/full.png",
    },
    "axe": {
        "cooldown": 400,
        "damage": 30,
        "graphic": "./graphics/weapons/axe/full.png",
    },
    "lance": {
        "cooldown": 400,
        "damage": 30,
        "graphic": "./graphics/weapons/lance/full.png",
    },
    "rapier": {
        "cooldown": 50,
        "damage": 8,
        "graphic": "./graphics/weapons/rapier/full.png",
    },
    "sai": {
        "cooldown": 80,
        "damage": 10,
        "graphic": "./graphics/weapons/sai/full.png",
    },
}

magicData = {
    "flame": {
        "strength": 5,
        "cost": 20,
        "graphic": "./graphics/particles/flame/fire.png",
    },
    "heal": {
        "strength": 20,
        "cost": 10,
        "graphic": "./graphics/particles/heal/heal.png",
    },
}
