import omni.replicator.core as rep
with rep.new_layer():

    # Add Default Light
    distance_light = rep.create.light(rotation=(315,0,0), intensity=3000, light_type="distant")

    #render_product = rep.create.render_product('/World/Camera_01', (2048, 1024))
    camera = rep.create.camera(focus_distance=200,f_stop=5.0)
    camera2 = rep.create.camera(focus_distance=200,f_stop=5.0)
    camera3 = rep.create.camera(focus_distance=200,f_stop=5.0)

    def tennis_paddle():
        tennis_paddle = rep.get.prims(path_pattern='/World/fruits_living_room/tennis_paddle_1')
        with tennis_paddle:
            rep.modify.semantics([('class', 'Table Tennis paddle')])
            rep.modify.pose(
                position = (66.4, 111.387, 1001.32),
                rotation = (-8.11, -68.42, 7.601),
                )
        return tennis_paddle.node

    def game_board():
        game_board = rep.get.prims(path_pattern='/World/fruits_living_room/Checker_board')
        with game_board:
            rep.modify.semantics([('class', 'Game board')])
            rep.modify.pose(
                position = (-130.73, 200.24, 447.50),
                rotation = (0, 0, 0),
                )
        return game_board.node
        

    def comb():
        comb = rep.get.prims(path_pattern='/World/fruits_living_room/Lowpoly_Sharp_Comb')
        with comb:
            rep.modify.semantics([('class', 'Comb')])
            rep.modify.pose(
                position = (-113.63, 211.83, 250.486),
                rotation = (-348.122, 4.478, 90.850),
                )
        return comb.node


    def pom_1():
        pom_1 = rep.get.prims(path_pattern='/World/fruits_living_room/Pomegranate')
        with pom_1:
            rep.modify.semantics([('class', 'Pomegranate')])
            rep.modify.pose(
                position = (146.08, 90.28, -169.107),
                rotation = (-327.537, 73.934, 50.832),
                )
        return pom_1.node


    def pom_2():
        pom_2 = rep.get.prims(path_pattern='/World/fruits_living_room/Pomegranate___Metashape')
        with pom_2:
            rep.modify.semantics([('class', 'Pomegranate')])
            rep.modify.pose(
                position = (111.264, 114.787, 1284.755),
                rotation = (47.19, 4.482,-93.964),
                )
        return pom_2.node

    def papaya():
        papaya = rep.get.prims(path_pattern='/World/fruits_living_room/Papaya')
        with papaya:
            rep.modify.semantics([('class', 'Papaya')])
            rep.modify.pose(
                position = (126.10, 119.223, 1173.28),
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
    render_product2 = rep.create.render_product(camera2, (1024, 1024))
    render_product3 = rep.create.render_product(camera3, (1024, 1024))
    
    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(output_dir="C:/omniverse/output", rgb=True, bounding_box_2d_tight=True, distance_to_camera=True, distance_to_image_plane=True, normals=True)
    writer.attach([render_product, render_product2, render_product3])
    
    
    # Setup randomization
    with rep.trigger.on_frame(num_frames=600):
        rep.randomizer.tennis_paddle()
        rep.randomizer.game_board()
        rep.randomizer.comb()
        rep.randomizer.pom_1()
        rep.randomizer.pom_2()
        rep.randomizer.papaya()
        with camera:
            rep.modify.pose(position=rep.distribution.uniform((1000, 500, 900), (1480, 894, 1605)), look_at=("/World/fruits_living_room/Appleseed_CoffeeTable", "/World/fruits_living_room/Pomegranate___Metashape"))
        with camera2:
            rep.modify.pose(position=rep.distribution.uniform((961, 742, 1000), (1185, 945, 2000)), look_at=("/World/fruits_living_room/Books_Cabinet", "/World/fruits_living_room/Appleseed_CoffeeTable"))
        with camera3:
            rep.modify.pose(position=rep.distribution.uniform((700, 600, 400), (1721, 968.2, 730.8)), look_at=("/World/fruits_living_room/Appleseed_CoffeeTable", "/World/fruits_living_room/Checker_board"))
