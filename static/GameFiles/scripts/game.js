class Example extends Phaser.Scene
    {
        //might have to declare somewhere the bg
        constructor(bg, trees, wind, fg){
            super({key: 'Game'});
            this.bg = bg;
            this.trees = trees;
            this.wind = wind;
            this.fg = fg;
            this.AssetKeys = {
                //idk makes it easier to access
                BACKGROUND: "forest_background",
                WIND: "wind",
                FOREGROUND: "forest_foreground",
                TREES: "trees",
            }
        }
        preload ()
        {
            // this.load.setBaseURL('https://cdn.phaserfiles.com/v385');

            // this.load.image('sky', sky);
            // this.load.image('logo', logo);
            // this.load.image('red', particle);
            this.load.image(this.AssetKeys.WIND, wind);
            this.load.image(this.AssetKeys.TREES, trees);
            this.load.image(this.AssetKeys.BACKGROUND, forest_background);
            this.load.image(this.AssetKeys.FOREGROUND, forest_foreground);
        }

        create ()
        {
            //get current width and height of current game
            //grabs direct reference
            const {width, height} = this.scale;
            //TODO: MAKE LONGER by 500ish
            this.bg = this.add.tileSprite(width+100,height-680, width, height, this.AssetKeys.BACKGROUND).setScale(2.5);
            this.trees = this.add.tileSprite(width+100,height-680, width, height, this.AssetKeys.TREES).setScale(2.5);
            this.fg = this.add.tileSprite(width+100,height-680, width, height, this.AssetKeys.FOREGROUND).setScale(2.5);
            //this.wind = this.add.tileSprite(width+100,height-680, width, height, this.AssetKeys.WIND).setScale(2.5);

            //this.add.image(400, 300, 'trees');

            // const particles = this.add.particles(0, 0, 'red', {
            //     speed: 100,
            //     scale: { start: 1, end: 0 },
            //     blendMode: 'ADD'
            // });

            // const logo = this.physics.add.image(400, 100, 'logo');

            // logo.setVelocity(100, 200);
            // logo.setBounce(1, 1);
            // logo.setCollideWorldBounds(true);

            // particles.startFollow(logo);
        }
        update(time, delta){
            this.bg.tilePositionX -=0.1;
            this.trees.tilePositionX -=0.2;
            this.fg.tilePositionX -=0.3;
            //might like it better without the wind, the wind sucks
         //   this.wind.tilePositionX -=0.4;

        }
    }

    const config = {
        type: Phaser.CANVAS,
     
        scene: Example,
        scale:{
            parent: 'game-container',
            width: 1545,
            height: 890,
        },
        backgroundColor: '#5c5b5b',
        // physics: {
        //     default: 'arcade',
        //     arcade: {
        //         gravity: { y: 200 }
        //     }
        // }
    };

    const game = new Phaser.Game(config);