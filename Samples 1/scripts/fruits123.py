import omni.replicator.core as rep
with rep.new_layer():

    # Add Default Light
    distance_light = rep.create.light(rotation=(315,0,0), intensity=3000, light_type="distant")

    #render_product = rep.create.render_product('/World/Camera_01', (2048, 1024))
    camera = rep.create.camera(focus_distance=200,f_stop=5.0)

    def tennis_paddle():
        tennis_paddle = rep.get.prims(path_pattern='/World/tennis_paddle_1')
        with tennis_paddle:
            rep.modify.semantics([('class', 'Table Tennis paddle')])
            rep.modify.pose(
                position = (-214.79, 134.169, 1286.06),
                rotation = (-16.03, -9.812, -31.88),
                )
        return tennis_paddle.node

    def game_board():
        game_board = rep.get.prims(path_pattern='/World/Checker_board')
        with game_board:
            rep.modify.semantics([('class', 'Game board')])
            rep.modify.pose(
                position = (98.94, 103.1555, 1075.87067),
                rotation = (0.061, 0.1034, 0.06301),
                )
        return game_board.node
        

    def comb():
        comb = rep.get.prims(path_pattern='/World/Lowpoly_Sharp_Comb')
        with comb:
            rep.modify.semantics([('class', 'Comb')])
            rep.modify.pose(
                position = (47.884, 111.374, 1271.769),
                rotation = (-168.23, -1.321, 90.315),
                )
        return comb.node


    def pom_1():
        pom_1 = rep.get.prims(path_pattern='/World/Pomegranate')
        with pom_1:
            rep.modify.semantics([('class', 'Pomegranate')])
            rep.modify.pose(
                position = (707.20, 188.51, 1707.877),
                rotation = (9.385, -58.875, -0.657),
                )
        return pom_1.node


    def pom_2():
        pom_2 = rep.get.prims(path_pattern='/World/Pomegranate___Metashape')
        with pom_2:
            rep.modify.semantics([('class', 'Pomegranate')])
            rep.modify.pose(
                position = (825.65, 236.76, 1611.94),
                rotation = (-1.2482, 0,0),
                )
        return pom_2.node

    def papaya():
        papaya = rep.get.prims(path_pattern='/World/Papaya')
        with papaya:
            rep.modify.semantics([('class', 'Papaya')])
            rep.modify.pose(
                position = (596.741, 213.21, 1533.353),
                rotation = (0.927, -210.23, -0.434),
                )
        return papaya.node


    rep.randomizer.register(tennis_paddle)
    rep.randomizer.register(game_board)
    rep.randomizer.register(comb)
    rep.randomizer.register(pom_1)
    rep.randomizer.register(pom_2)
    rep.randomizer.register(papaya)
    
    render_product = rep.create.render_product(camera, (1024, 1024))
    
    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(output_dir="C:/omniverse/output", rgb=True, bounding_box_2d_tight=True)
    writer.attach([render_product])
    
    
    # Setup randomization
    with rep.trigger.on_frame(num_frames=20):
        rep.randomizer.tennis_paddle()
        rep.randomizer.game_board()
        rep.randomizer.comb()
        rep.randomizer.pom_1()
        rep.randomizer.pom_2()
        rep.randomizer.papaya()
        with camera:
            rep.modify.pose(position=rep.distribution.uniform((961, 742, 211), (1061, 850, 400)), look_at=("/World/Appleseed_CoffeeTable")) 