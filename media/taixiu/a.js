/// <reference path="commongame.js" />
var LuckyDiceGame = LuckyDiceGame || {};
var LuckyDiceHub = LuckyDiceHub || {};
var luckyDiceConfig;
var luckyDiceLoaderVer = "?=1.0.1.1.22";
if (window.location.href.indexOf("http://localhost:58917/") > -1) {
    luckyDiceConfig = {
        Url_Root: "http://localhost:58917/",
        Hub_Url: "http://localhost:58917/",
        hubName: "miniGameHub",
        Api_call_TanLoc: "//vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocTanLoc?prizeValue=",
        GetSessionDetailUrl: "//vuachoibai.com/event/api/LuckyDiceApi/",
        Url_GetPointRutLoc: "//vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocGetPoint",
        Url_GetVinhDanhTanLocMarquee: "//vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocVinhDanh?type=5",
        Url_SelectRutLoc: "//vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocRutLoc",
        Url_GetResultRutLoc: "//vuachoibai.com/event/Api/EventTaiXiu092015/GetAwardPrizeRutLoc",
        Url_Api: "aaaa",
        Type: 1
    };
} else if (window.location.href.indexOf("http://alpha.vuachoibai.com/") > -1) {
    luckyDiceConfig = {
        Url_Root: "http://alpha.vuachoibai.com/luckydice/",
        Hub_Url: "//alpha.vuachoibai.com/miniluckydice",
        hubName: "miniGameHub",
        Api_call_TanLoc: "EventTaiLocTanLoc?prizeValue=",
        GetSessionDetailUrl: "//alpha.vuachoibai.com/event/api/LuckyDiceApi/",
        Url_GetPointRutLoc: "//alpha.vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocGetPoint",
        Url_GetVinhDanhTanLocMarquee: "//alpha.vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocVinhDanh?type=5",
        Url_SelectRutLoc: "//alpha.vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocRutLoc",
        Url_GetResultRutLoc: "//alpha.vuachoibai.com/event/Api/EventTaiXiu092015/GetAwardPrizeRutLoc",
        Url_Api: "/minigames/api/luckydice/",
        Type: 2
    };
}  else if (window.location.href.indexOf("http://beta.vuachoibai.com/") > -1) {
    luckyDiceConfig = {
        Url_Root: "http://beta.vuachoibai.com/miniluckydice/",
        Hub_Url: "//betamini.vuachoibai.com/luckydice",
        hubName: "miniGameHub",
        Api_call_TanLoc: "//betamini.vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocTanLoc?prizeValue=",
        GetSessionDetailUrl: "//betamini.vuachoibai.com/event/api/LuckyDiceApi/",
        Url_GetPointRutLoc: "//betamini.vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocGetPoint",
        Url_GetVinhDanhTanLocMarquee: "//betamini.vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocVinhDanh?type=5",
        Url_SelectRutLoc: "//betamini.vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocRutLoc",
        Url_GetResultRutLoc: "//betamini.vuachoibai.com/event/Api/EventTaiXiu092015/GetAwardPrizeRutLoc",
        Url_Api: "//beta.vuachoibai.com/clientminigame/api/luckydice/",
        Type: 2
    };
} else if (window.location.href.indexOf("http://vuachoibai.com/") > -1) {
    luckyDiceConfig = {
        Url_Root: "http://vuachoibai.com/miniluckydice/",
        Hub_Url: "//txw.vuachoibai.com/",
        hubName: "miniGameHub",
        Api_call_TanLoc: "//vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocTanLoc?prizeValue=",
        GetSessionDetailUrl: "//vuachoibai.com/event/api/LuckyDiceApi/",
        Url_GetPointRutLoc: "//vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocGetPoint",
        Url_GetVinhDanhTanLocMarquee: "//vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocVinhDanh?type=5",
        Url_SelectRutLoc: "//vuachoibai.com/event/Api/EventTaiXiu092015/EventTaiLocRutLoc",
        Url_GetResultRutLoc: "//vuachoibai.com/event/Api/EventTaiXiu092015/GetAwardPrizeRutLoc",
        Url_Api: "//vuachoibai.com/clientminigame/api/luckydice/",
        Type: 2
    };
} else if (window.location.href.indexOf("http://vuachoibai.net/") > -1) {
    luckyDiceConfig = {
        Url_Root: "http://vuachoibai.net/miniluckydice/",
        Hub_Url: "//txw.vuachoibai.net/",
        hubName: "miniGameHub",
        Api_call_TanLoc: "//vuachoibai.net/event/Api/EventTaiXiu092015/EventTaiLocTanLoc?prizeValue=",
        GetSessionDetailUrl: "//vuachoibai.net/event/api/LuckyDiceApi/",
        Url_GetPointRutLoc: "//vuachoibai.net/event/Api/EventTaiXiu092015/EventTaiLocGetPoint",
        Url_GetVinhDanhTanLocMarquee: "//vuachoibai.net/event/Api/EventTaiXiu092015/EventTaiLocVinhDanh?type=5",
        Url_SelectRutLoc: "//vuachoibai.net/event/Api/EventTaiXiu092015/EventTaiLocRutLoc",
        Url_GetResultRutLoc: "//vuachoibai.net/event/Api/EventTaiXiu092015/GetAwardPrizeRutLoc",
        Url_Api: "//vuachoibai.net/clientminigame/api/luckydice/",
        Type: 2
    };
} else if (window.location.href.indexOf("http://vuachoibai.org/") > -1) {
    luckyDiceConfig = {
        Url_Root: "http://vuachoibai.org/miniluckydice/",
        Hub_Url: "//txw.vuachoibai.org/",
        hubName: "miniGameHub",
        Api_call_TanLoc: "//vuachoibai.org/event/Api/EventTaiXiu092015/EventTaiLocTanLoc?prizeValue=",
        GetSessionDetailUrl: "//vuachoibai.org/event/api/LuckyDiceApi/",
        Url_GetPointRutLoc: "//vuachoibai.org/event/Api/EventTaiXiu092015/EventTaiLocGetPoint",
        Url_GetVinhDanhTanLocMarquee: "//vuachoibai.org/event/Api/EventTaiXiu092015/EventTaiLocVinhDanh?type=5",
        Url_SelectRutLoc: "//vuachoibai.org/event/Api/EventTaiXiu092015/EventTaiLocRutLoc",
        Url_GetResultRutLoc: "//vuachoibai.org/event/Api/EventTaiXiu092015/GetAwardPrizeRutLoc",
        Url_Api: "//vuachoibai.org/clientminigame/api/luckydice/",
        Type: 2
    };
}

(function (scope, $) {
    var luckyDiceHub = function (hub) {
        hub.server = {};
        hub.client = {};
        $.extend(hub.server, {
            getCurrentRooms: function (betType) {
                return hub.invoke.apply(hub, $.merge(["getCurrentRooms"], $.makeArray(arguments)));
            },
            setBet: function (betType, gate, amount) {
                return hub.invoke.apply(hub, $.merge(["setBet"], $.makeArray(arguments)));
            },
            GetBetOfAccount: function (betType) {
                return hub.invoke.apply(hub, $.merge(["GetBetOfAccount"], $.makeArray(arguments)));
            },
            GetCurrentResult: function () {
                return hub.invoke.apply(hub, $.merge(["GetCurrentResult"], $.makeArray(arguments)));
            },
            GetAccountResult: function (gameSessionId) {
                return hub.invoke.apply(hub, $.merge(["GetAccountResult"], $.makeArray(arguments)));
            },
            HideDice: function () {
                return hub.invoke.apply(hub, $.merge(["HideDice"], $.makeArray(arguments)));
            }
        });

        hub.on('currentSession', function (data) {
            //console.debug('session', data);
            if (typeof LuckyDiceGame != 'undefined' && typeof LuckyDiceGame.UpdateSession == 'function')
                LuckyDiceGame.UpdateSession(data);
        });

        hub.on('currentResult', function (data) {
            //console.debug('result', data);
            if (typeof LuckyDiceGame != 'undefined' && typeof LuckyDiceGame.UpdateResult == 'function')
                LuckyDiceGame.UpdateResult(data);
        });

        hub.on('currentRoomsInfo', function (data) {
            //console.debug('roomInfo', data);
            if (typeof LuckyDiceGame != 'undefined' && typeof LuckyDiceGame.UpdateRoomInfo == 'function')
                LuckyDiceGame.UpdateRoomInfo(data);
        });

        hub.on('betOfAccount', function (data, balance) {
            //console.debug('UpdateBetOfAccount', data, balance);
            if (typeof LuckyDiceGame != 'undefined' && typeof LuckyDiceGame.UpdateBetOfAccount == 'function')
                LuckyDiceGame.UpdateBetOfAccount(data, balance);
        });

        hub.on('resultOfAccount', function (data) {
            //console.debug('ResultOfAccount', data);
            if (typeof LuckyDiceGame != 'undefined' && typeof LuckyDiceGame.ResultOfAccount == 'function')
                LuckyDiceGame.ResultOfAccount(data);
        });

        hub.on('gameHistory', function (data) {
            //console.debug('ShowGameHistory', data);
            if (typeof LuckyDiceGame != 'undefined' && typeof LuckyDiceGame.ShowGameHistory == 'function')
                LuckyDiceGame.ShowGameHistory(data);
        });
    }
    scope.LuckyDiceHub = luckyDiceHub;
})(window, $);

(function (scope, $) {

    var luckyDiceLogic = function () {
        this.isRoom = 1;
        this.rowperPage = 10;
        this.cacheData = null;
        this.isBet = true;

        this.isInEvent = false;
        this.timeLeftTl = 0;
        this.totalPointTl = 0;
        this.intevalCountDownTl = 0;
        this.dkRutLoc = 0;

        this.moneyTanLoc = 0;
        this.top20Data = null;
        this.isBettingTx = false;

        this.dice01 = 0;
        this.dice02 = 0;
        this.dice03 = 0;
        this.isEnter = false;

        this.InitGame();
    }

    luckyDiceLogic.prototype.InitGame = function () {
        this.hubUrl = luckyDiceConfig.Hub_Url;
        this.connection = $.hubConnection(this.hubUrl);
        this.gameLuckyDiceHub = this.connection.createHubProxy(luckyDiceConfig.hubName);
        this.luckyDiceHub = new scope.LuckyDiceHub(this.gameLuckyDiceHub);

        this.connection.stateChanged(function (change) {
            if (change.newState === $.signalR.connectionState.connecting) {
                console.info('minigame luckyDice reconnecting');
            } else if (change.newState === $.signalR.connectionState.reconnecting) {
                console.info('minigame luckyDice reconnecting');
            } else if (change.newState === $.signalR.connectionState.connected) {
                console.info('minigame luckyDice connected');
            } else if (change.newState === $.signalR.connectionState.disconnected) {
                console.info('minigame luckyDice disconnected');
                LuckyDiceGame.ReconnectHubLuckyDice();
            }
        });
    }

    luckyDiceLogic.prototype.StartHub = function () {
        try {
            this.connection.start({ transport: 'longPolling', jsonp: true, waitForPageLoad: true }).done(function () {
                LuckyDiceGame.LoadResources();
            }).fail(function () {
                LuckyDiceGame.ReconnectHubLuckyDice();
            });
        } catch (e) {
            LuckyDiceGame.ReconnectHubLuckyDice();
        }
    }

    luckyDiceLogic.prototype.ReStartHub = function () {
        try {
            this.connection.start({ transport: 'longPolling', jsonp: true, waitForPageLoad: true }).done(function () {
            }).fail(function () {
                LuckyDiceGame.ReconnectHubLuckyDice();
            });
        } catch (e) {
            LuckyDiceGame.ReconnectHubLuckyDice();
        }
    }

    luckyDiceLogic.prototype.StopHub = function () {
        this.connection.stop();
        console.log('minigame luckyDice disconnected');
    }

    luckyDiceLogic.prototype.ReconnectHubLuckyDice = function () {
        if (typeof disconnect != 'underfined') {
            clearInterval(disconnect);
            delete disconnect;
        }
        var disconnect = setInterval(function () {
            if (LuckyDiceGame.connection.state == $.signalR.connectionState.disconnected) {
                LuckyDiceGame.connection.start({ transport: 'longPolling', jsonp: true, waitForPageLoad: true }).done(function () {
                    clearInterval(disconnect);
                    delete disconnect;
                });
            }
        }, 5000);
    }

    luckyDiceLogic.prototype.ShowLuckyDice = function () {
        this.StartHub();
        //LuckyDiceGame.LoadResources();
    }

    luckyDiceLogic.prototype.ShowHideLuckyDice = function () {
        if (typeof LuckyDiceGame == 'undefined')
            return;

        if ($('#allGameLuckyDice').css('display') == 'none') {
            LuckyDiceGame.ShowDiceGUI();
            window.localStorage.setItem("showhidetx", "1");
            if (ga && ga !== undefined) {
                ga('send', 'event', 'Minigame', 'Tà€i xì‰u', 'Show');
            }
        }
        else {
            LuckyDiceGame.HideDiceGUI();
            window.localStorage.setItem("showhidetx", "0");
            if (ga && ga !== undefined) {
                ga('send', 'event', 'Minigame', 'Tà€i xì‰u', 'Hide');
            }
        }
    }

    luckyDiceLogic.prototype.ShowDiceGUI = function () {
        $('#allGameLuckyDice').show();
        $('#time').hide();
        this.CheckShowInTime();
        this.SelectRoom(this.isRoom);

        setTimeout(function () {
            if ($('#tx_box_chat_all').css('display') == 'none') {
                LuckydiceChat.RegisterChat();
            }
        }, 3000);
    }

    luckyDiceLogic.prototype.HideDiceGUI = function () {
        $('#allGameLuckyDice').hide();
        $('#time').show();
        try {
            LuckyDiceGame.gameLuckyDiceHub.server.HideDice();
        } catch (e) { }
    }

    luckyDiceLogic.prototype.UpdateSession = function (data) {
        if (data != null) {
            this.currentSession = data;
            this.sessionNow = data.GameSessionID;
            this.tickBet = data.RemainBetting;
            this.tickWait = data.RemainWaiting;

            $("#sessionidTX").html("PhiĂªn: " + data.GameSessionID);
        }
    }

    luckyDiceLogic.prototype.UpdateRoomInfo = function (data) {
        if (data.length > 0 && data != null && data[0] != '' && data[0] != undefined && data[0].BetType == this.isRoom) {
            $('#tx_money_xiu').html(LuckyDiceGame.FormatNumberTaiXiu(data[0].TotalBetValue1));
            $('#tx_poeple_xiu').html(data[0].TotalAccount1);
            $('#tx_money_tai').html(LuckyDiceGame.FormatNumberTaiXiu(data[0].TotalBetValue2));
            $('#tx_poeple_tai').html(data[0].TotalAccount2);
        }
    }

    luckyDiceLogic.prototype.UpdateResult = function (data) {
        if (data != null) {
            this.dice01 = data.Dice1;
            this.dice02 = data.Dice2;
            this.dice03 = data.Dice3;

            var that = this;
            $('#totalDiemPhien').hide();
            this.stageCanvas.getChildAt(1).alpha = 0;
            this.bg_bitmap.alpha = 0;
            this.textTime.alpha = 0;
            this.containerResult.removeAllChildren();
            var dataSpirte = new createjs.SpriteSheet({
                "images": [this.loadResources.getResult('xucxacEffect')],
                "frames": { "height": 140, "width": 140 },
                "animations": { "walk": [0, 40, "", 0.5] }
            });
            var imgSprite = new createjs.Sprite(dataSpirte, "walk");
            imgSprite.set({ name: 'character' });
            createjs.Ticker.timingMode = createjs.Ticker.RAF;
            this.containerResult.addChild(imgSprite);

            var checkTimeOut = false;
            var timeout = setTimeout(function () {
                if (checkTimeOut) {
                    return;
                } else {
                    that.containerResult.removeAllChildren();
                    that.stageCanvas.getChildAt(1).alpha = 1;
                    that.bg_bitmap.alpha = 0;
                    that.ShowDice(that.isEffect);
                }
            }, 2222);

            var timeout02 = setTimeout(function () {
                that.ShowDice(that.isEffect);
            }, 1450);

            imgSprite.addEventListener('animationend', function () {
                checkTimeOut = true;
                clearTimeout(timeout);
                clearTimeout(timeout02);
                that.ShowDice(that.isEffect);
            });
        }
    }

    luckyDiceLogic.prototype.ShowDice = function () {
        var that = this;
        var number1 = new createjs.Bitmap(this.loadResources.getResult('result_xucxac'));
        number1.set({ sourceRect: new createjs.Rectangle((this.dice01 - 1) * 18, 0, 18, 20) });
        switch (this.dice01) {
            case 1: number1.scaleX = 0.7; number1.scaleY = 0.7; number1.x = 46; number1.y = 79; break;
            case 2: number1.scaleX = 0.9; number1.scaleY = 0.9; number1.x = 53; number1.y = 87; number1.regX = 10; number1.regY = 10; number1.rotation = -73; break;
            case 3: number1.scaleX = 0.9; number1.scaleY = 0.9; number1.x = 53; number1.y = 87; number1.regX = 10; number1.regY = 10; number1.rotation = -20; break;
            case 4: number1.scaleX = 0.9; number1.scaleY = 0.9; number1.x = 53; number1.y = 87; number1.regX = 10; number1.regY = 10; number1.rotation = -73; break;
            case 5: number1.scaleX = 0.9; number1.scaleY = 0.9; number1.x = 53; number1.y = 87; number1.regX = 10; number1.regY = 10; number1.rotation = -73; break;
            case 6: number1.scaleX = 0.9; number1.scaleY = 0.9; number1.x = 53; number1.y = 87; number1.regX = 10; number1.regY = 10; number1.rotation = -73; break;
            default: number1.scaleX = 0.9; number1.scaleY = 0.9; number1.x = 53; number1.y = 87; number1.regX = 10; number1.regY = 10; number1.rotation = -73; break;
        }

        var number2 = new createjs.Bitmap(this.loadResources.getResult('result_xucxac'));
        number2.set({ sourceRect: new createjs.Rectangle((this.dice02 - 1) * 18, 0, 18, 20) });
        if (this.dice02 != 1) {
            number2.scaleX = 0.9;
            number2.scaleY = 0.9;
        } else {
            number2.scaleX = 0.7;
            number2.scaleY = 0.7;
        }
        if (this.dice02 != 3) {
            number2.x = 51;//62
            number2.y = 46.5;//53.5
            number2.regX = 10;
            number2.regY = 10;
            number2.rotation = -20; //-20
        } else {
            number2.x = 50.5;//61.5
            number2.y = 46;//53
            number2.regX = 10;
            number2.regY = 10;
            number2.rotation = -70; //-70
        }

        var number3 = new createjs.Bitmap(this.loadResources.getResult('result_xucxac'));
        number3.set({ sourceRect: new createjs.Rectangle((this.dice03 - 1) * 18, 0, 18, 20) });
        if (this.dice03 != 1) {
            number3.scaleX = 0.9;
            number3.scaleY = 0.9;
        }
        else {
            number3.scaleX = 0.7;
            number3.scaleY = 0.7;
        }
        if (this.dice03 == 1) {
            number3.x = 80.7;//91.7
            number3.y = 62.5;//69.5
            number3.rotation = -33;
        }
        else if (this.dice03 != 3) {
            number3.x = 79;//90
            number3.y = 71;//78
            number3.rotation = -73;
        }
        else {
            number3.x = 79;//90
            number3.y = 63;//70
            number3.rotation = -33;
        }
        this.containerResult.addChild(number1, number2, number3);

        if (this.isEffect) {
            this.StartEffectOpenBowl(this.LastResult);
        } else {
            setTimeout(function () {
                LuckyDiceGame.LastResult();
            }, 500);
        }

    }

    luckyDiceLogic.prototype.LastResult = function () {
        if ((this.dice01 + this.dice02 + this.dice03) > 0 && (this.dice01 + this.dice02 + this.dice03) < 19) {
            $('#tx_totalDiemPhien').show();
            $('#tx_totalDiemPhien').html(this.dice01 + this.dice02 + this.dice03);
        }
        if ((this.dice01 + this.dice02 + this.dice03) > 10 && (this.dice01 + this.dice02 + this.dice03) < 19) $('#tx_cua_tai').addClass('animated');
        if ((this.dice01 + this.dice02 + this.dice03) > 0 && (this.dice01 + this.dice02 + this.dice03) < 11) $('#tx_cua_xiu').addClass('animated');
    }

    luckyDiceLogic.prototype.UpdateBetOfAccount = function (data, balance) {
        var betUnder = 0, betOver = 0;
        if (data != null) {
            for (var i = 0; i < data.length; i++) {
                if (data[i].LocationID == 1)//xiu
                    betUnder += parseInt(data[i].BetValue);
                else
                    betOver += parseInt(data[i].BetValue);
            }
        }
        $("#input_xiu_money_bottom").html(LuckyDiceGame.FormatNumber(betUnder));
        $("#input_tai_money_bottom").html(LuckyDiceGame.FormatNumber(betOver));

        if (luckyDiceConfig.Type != 1) {
            if (balance > -1 && App && App.currentAccount) {
                if (LuckyDiceGame.isRoom == 2) App.currentAccount.Coin = balance;
                else App.currentAccount.TotalStar = balance;

                AccountInfo.bindAccountInfo(App.currentAccount);
            }
        }
    }

    luckyDiceLogic.prototype.ResultOfAccount = function (data) {

        var sumStar = 0;
        var sumCoin = 0;
        var refundvalueStar = 0;
        var refundvalueCoin = 0;
        var winner = false;
        if (data.length > 0 && data != null && data[0] != '' && data[0] != undefined) {
            for (var i = 0; i < data.length; i++) {
                if (data[i].BetType == 1) {
                    sumStar = data[i].PrizeValue;
                    refundvalueStar += data[i].RefundValue;
                }
                if (data[i].BetType == 2) {
                    sumCoin = data[i].PrizeValue;
                    refundvalueCoin += data[i].RefundValue;
                }
            }
            if (sumStar > 0 || sumCoin > 0)
                winner = true;
        }
        this.ShowTextResult(sumStar, sumCoin, winner);

        if ((sumCoin + refundvalueCoin) > 0 || (sumStar + refundvalueStar) > 0) LuckyDiceGame.isMoneyResult = false;

        if (App && App.currentAccount) {
            App.currentAccount.Coin += sumCoin + refundvalueCoin;
            App.currentAccount.TotalStar += sumStar + refundvalueStar;

            AccountInfo.bindAccountInfo(App.currentAccount);
			// window.setTimeout(function(){
				// EventTX2016T5.GetAccountInfo();
			// }, 5000);
        }
    }

    luckyDiceLogic.prototype.ShowTextResult = function (sumStar, sumCoin, bool) {
        if ($("#allGameLuckyDice").css('display') == 'none') {

            $('#prizebet').css('top', '22px');
            $('#prizebet').css('opacity', '1');
            $('#prizebet').show();
            if (bool == true) {
                if (sumStar > 0 && sumCoin > 0) {
                    var html = '<p style="color:#fff000">+' + LuckyDiceGame.FormatNumber(sumStar) + '</p><p style="color:#FFFFFF">+' + LuckyDiceGame.FormatNumber(sumCoin) + '</p>';
                    $('#prizebet').html((LuckyDiceGame.dice01 + LuckyDiceGame.dice02 + LuckyDiceGame.dice03) >= 11 ? ("TĂ i " + html) : ("Xá»‰u " + html));
                }
                else if (sumStar > 0) {
                    var html = ' <p style="color:#fff000"> +' + LuckyDiceGame.FormatNumber(sumStar) + '</p>';
                    $('#prizebet').html((LuckyDiceGame.dice01 + LuckyDiceGame.dice02 + LuckyDiceGame.dice03) >= 11 ? ("TĂ i " + html) : ("Xá»‰u " + html));
                }
                else if (sumCoin > 0) {
                    var html = ' <p style="color:#FFFFFF">+' + LuckyDiceGame.FormatNumber(sumCoin) + '</p>';
                    $('#prizebet').html((LuckyDiceGame.dice01 + LuckyDiceGame.dice02 + LuckyDiceGame.dice03) >= 11 ? ("TĂ i " + html) : ("Xá»‰u " + html));
                }
            }
            else $('#prizebet').text((LuckyDiceGame.dice01 + LuckyDiceGame.dice02 + LuckyDiceGame.dice03) >= 11 ? "TĂ i" : "Xá»‰u");
            $('#prizebet').animate({ top: '0px', opacity: 0 }, 5000);
        }
        else {
            if (bool == true) {
                $('#prizebet').css('top', '22px');
                $('#prizebet').css('opacity', '1');
                $('#prizebet').show();
                if (sumStar > 0 && sumCoin > 0) {
                    var html = '<p style="color:#fff000">+' + LuckyDiceGame.FormatNumber(sumStar) + '</p><p style="color:#FFFFFF">+' + LuckyDiceGame.FormatNumber(sumCoin) + '</p>';
                    $('#prizebet').html(html);
                }
                else if (sumStar > 0) {
                    var html = '<p style="color:#fff000">+' + LuckyDiceGame.FormatNumber(sumStar) + '</p>';
                    $('#prizebet').html(html);
                }
                else if (sumCoin > 0) {
                    var html = '<p style="color:#FFFFFF">+' + LuckyDiceGame.FormatNumber(sumCoin) + '</p>';
                    $('#prizebet').html(html);

                }
                $('#prizebet').animate({ top: '0px', opacity: 0 }, 5000);
            }
        }
    }

    // cáº­p nháº­t 15 phiĂªn gáº§n nháº¥t
    luckyDiceLogic.prototype.ShowGameHistory = function (data) {
        if (data != null) {
            if ($('#LuckyDiceSoiCau').css('display') == 'block') {
                $.ajax({
                    type: "GET",
                    url: luckyDiceConfig.Url_Root + 'MiniGameLuckyDice/LuckyDiceSoiCau',
                    success: function (data) {
                        $('#LuckyDiceSoiCau').show();
                        $('#LuckyDiceSoiCau').html(data);
                    },
                    fail: function (fail) {
                        console.log('loi nhe');
                    }
                });
            }
            $('#listSoiCauTX').html('');
            var string = '';
            for (var i = data.length - 1; i >= 0; i--) {
                var tooltip = (data[i].DiceSum) + ' (' + data[i].Dice1 + ' ' + data[i].Dice2 + ' ' + data[i].Dice3 + ')';
                if (data[i].LocationIDWin == 2)//tai
                {
                    if (i == 0)
                        string += '<li onclick=LuckyDiceGame.GetTop20(' + data[i].GameSessionID + ') title="TĂ i: ' + tooltip + '" style="margin-left: 0px;"><img src="' + luckyDiceConfig.Url_Root + 'images/icon_bong3.png" alt=""></li>';
                    else
                        string += '<li onclick=LuckyDiceGame.GetTop20(' + data[i].GameSessionID + ')  title="TĂ i: ' + tooltip + '"><img src="' + luckyDiceConfig.Url_Root + 'images/icon_bong2.png" alt=""></li>';
                }
                else {
                    if (i == 0)
                        string += '<li onclick=LuckyDiceGame.GetTop20(' + data[i].GameSessionID + ')  title="Xá»‰u: ' + tooltip + '" style="margin-left: 0px;"><img src="' + luckyDiceConfig.Url_Root + 'images/icon_bongtrang_cau.png" alt=""></li>'
                    else
                        string += '<li onclick=LuckyDiceGame.GetTop20(' + data[i].GameSessionID + ')  title="Xá»‰u: ' + tooltip + '"><img src="' + luckyDiceConfig.Url_Root + 'images/icon_bong1.png" alt=""></li>'
                }
            }
            $('#listSoiCauTX').html(string);
        }
    }

    luckyDiceLogic.prototype.SetPopup = function (width, height, html) {
        if ($("#Popup_Container_tx").length > 0) {
            $("#temPopup_tx").html(html);
        }
        else {
            var htmlStr = '<div id="Popup_Container_tx" style="width:' + width + 'px;">' +
                              '<div  id="popup_nd">' +
                              '<div id="temPopup_tx">' + html +
                              '</div></div></div>' +
                              '<div onclick="LuckyDiceGame.ClosePopup();" id="overlayxx_tx" class="overlay"></div>';

            $('body').append(htmlStr);


            $('#popup_nd_tx').css('width', width);
            $('#popup_nd_tx').css('height', height);
            var leftOffset = ($(window).width() - width) / 2;
            var topOffset = ($(window).height() - height) / 2 + $(window).scrollTop();
            $('#Popup_Container_tx').css('left', leftOffset);
            $('#Popup_Container_tx').css("top", topOffset);
            $('#Popup_Container_tx').css('z-index', 1300);
            $('#Popup_Container_tx').css('position', 'absolute');
            $('#overlayxx_tx').css('height', $(document).height());
            $('#overlayxx_tx').show();
        }

        $("#Popup_Container_tx").draggable();
    }

    luckyDiceLogic.prototype.ClosePopup = function () {
        $('#Popup_Container_tx').remove();
        $('#overlayxx_tx').remove();
        $('.popup').remove();
        $('.overlay').remove();
    }

    luckyDiceLogic.prototype.ShowGuiGame = function () {
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.Url_Root + 'MiniGameLuckyDice/LuckyDiceGuide',
            success: function (data) {
                LuckyDiceGame.SetPopup(480, 315, data);
                $('#textGuide').mCustomScrollbar({ autoHideScrollbar: true, advanced: { updateOnContentResize: true } });
            },
            fail: function (fail) {
                console.log('loi nhe');
            }
        });
    }

    luckyDiceLogic.prototype.ShowHideSoiCau = function () {

        if ($('#LuckyDiceSoiCau').css('display') == 'block') {
            $('#LuckyDiceSoiCau').hide();
        } else {
            $.ajax({
                type: "GET",
                url: luckyDiceConfig.Url_Root + 'MiniGameLuckyDice/LuckyDiceSoiCau',
                success: function (data) {
                    $('#LuckyDiceSoiCau').show();
                    $('#LuckyDiceSoiCau').html(data);
                },
                fail: function (fail) {
                    console.log('loi nhe');
                }
            });
        }
    }

    luckyDiceLogic.prototype.ShowRank = function (tabIndex, tabRoom) {
        if (tabIndex == 2 && tabRoom == 2) {
            return;
        } else if (tabIndex == 3 && tabRoom == 2) {
            return;
        } else {
            if (tabIndex == 1) {
                this.BindRankGame(tabRoom);
            } else {
                $.ajax({
                    type: "GET",
                    url: luckyDiceConfig.Url_Root + 'MiniGameLuckyDice/LuckyDiceRanking?tabIndex=' + tabIndex + '&tabRoom=' + tabRoom,
                    success: function (data) {
                        LuckyDiceGame.SetPopup(780, 448, data);
                    },
                    fail: function (fail) {
                        console.log('loi nhe');
                    }
                });
            }
        }
    }

    luckyDiceLogic.prototype.BindRankGame = function (tabRoom) {
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.Url_Api + "GetTopDailyWinners?BetType=" + tabRoom + "&TopCount=10&r=" + Math.random(),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            crossDomain: true,
            xhrFields: {
                withCredentials: true
            },
            success: function (data) {
                if (data != null) {
                    var rankData = data;
                    $.ajax({
                        type: "GET",
                        url: luckyDiceConfig.Url_Root + 'MiniGameLuckyDice/LuckyDiceRanking?tabIndex=1&tabRoom=' + tabRoom,
                        success: function (data) {
                            LuckyDiceGame.SetPopup(780, 448, data);

                            var string = '';
                            string += '<tr>';
                            string += '<td>STT</td>';
                            string += '<td>TĂ i khoáº£n</td>';
                            string += '<td>Tiá»n tháº¯ng</td>';
                            string += '</tr>';

                            string += '<tr>';
                            string += '<td><img src="' + luckyDiceConfig.Url_Root + 'images/icon_stt1.png"></td>';
                            string += '<td>' + rankData[0].Username + '</td>';
                            string += '<td>' + LuckyDiceGame.FormatNumberTaiXiu(rankData[0].PrizeValue) + '</td>';
                            string += '</tr>';

                            string += '<tr>';
                            string += '<td><img src="' + luckyDiceConfig.Url_Root + 'images/icon_stt2.png"></td>';
                            string += '<td>' + rankData[1].Username + '</td>';
                            string += '<td>' + LuckyDiceGame.FormatNumberTaiXiu(rankData[1].PrizeValue) + '</td>';
                            string += '</tr>';

                            string += '<tr>';
                            string += '<td><img src="' + luckyDiceConfig.Url_Root + 'images/icon_stt3.png"></td>';
                            string += '<td>' + rankData[2].Username + '</td>';
                            string += '<td>' + LuckyDiceGame.FormatNumberTaiXiu(rankData[2].PrizeValue) + '</td>';
                            string += '</tr>';

                            for (var i = 3; i < rankData.length; i++) {
                                string += '<tr>';
                                string += '<td>' + (i + 1) + '</td>';
                                string += '<td>' + rankData[i].Username + '</td>';
                                string += '<td>' + LuckyDiceGame.FormatNumberTaiXiu(rankData[i].PrizeValue) + '</td>';
                                string += '</tr>';
                            }
                            $('#tx_listRankGame').html(string);

                            if (tabRoom == 1) $('#tx_listRankGame').css('color', '#ffb72f');
                            else $('#tx_listRankGame').css('color', 'white');
                        },
                        fail: function (fail) {
                            console.log('loi nhe');
                        }
                    });
                }
            }
        });
    }

    luckyDiceLogic.prototype.ShowHistory = function (tabRoom, current) {
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.Url_Api + "GetAccountHistory/?BetType=" + tabRoom + "&TopCount=500&r=" + Math.random(),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            crossDomain: true,
            xhrFields: {
                withCredentials: true
            },
            success: function (data) {
                if (data != null) {
                    LuckyDiceGame.cacheData = data;
                    LuckyDiceGame.BindHistory(tabRoom, current);
                }
            }
        });
        //LuckyDiceGame.cacheData = [{ "GameSessionID": 745429, "StartTime": "2016-05-31T11:39:00", "LocationName": "TĂ i", "Result": "1 - 4 - 2  7", "TotalBetValue": 4791, "RefundValue": 0, "PrizeValue": 0 }, { "GameSessionID": 745377, "StartTime": "2016-05-31T10:21:00", "LocationName": "Xá»‰u", "Result": "1 - 5 - 2  8", "TotalBetValue": 2420, "RefundValue": 0, "PrizeValue": 4791 }, { "GameSessionID": 744358, "StartTime": "2016-05-30T08:52:30", "LocationName": "TĂ i", "Result": "4 - 5 - 6  15", "TotalBetValue": 2000, "RefundValue": 0, "PrizeValue": 3960 }, { "GameSessionID": 737662, "StartTime": "2016-05-23T09:28:30", "LocationName": "Xá»‰u", "Result": "5 - 4 - 1  10", "TotalBetValue": 1020, "RefundValue": 1020, "PrizeValue": 0 }, { "GameSessionID": 734876, "StartTime": "2016-05-20T11:49:30", "LocationName": "Xá»‰u", "Result": "6 - 4 - 5  15", "TotalBetValue": 1000, "RefundValue": 0, "PrizeValue": 0 }, { "GameSessionID": 732881, "StartTime": "2016-05-18T09:57:00", "LocationName": "Xá»‰u", "Result": "5 - 2 - 5  12", "TotalBetValue": 300, "RefundValue": 0, "PrizeValue": 0 }, { "GameSessionID": 727420, "StartTime": "2016-05-12T17:25:30", "LocationName": "Xá»‰u", "Result": "2 - 5 - 4  11", "TotalBetValue": 1000, "RefundValue": 1000, "PrizeValue": 0 }, { "GameSessionID": 713651, "StartTime": "2016-04-28T09:12:00", "LocationName": "Xá»‰u", "Result": "4 - 3 - 4  11", "TotalBetValue": 324, "RefundValue": 0, "PrizeValue": 0 }, { "GameSessionID": 713650, "StartTime": "2016-04-28T09:10:30", "LocationName": "Xá»‰u", "Result": "1 - 3 - 3  7", "TotalBetValue": 164, "RefundValue": 0, "PrizeValue": 324 }, { "GameSessionID": 713638, "StartTime": "2016-04-28T08:52:30", "LocationName": "Xá»‰u", "Result": "2 - 3 - 3  8", "TotalBetValue": 83, "RefundValue": 0, "PrizeValue": 164 }, { "GameSessionID": 713496, "StartTime": "2016-04-28T05:19:30", "LocationName": "Xá»‰u", "Result": "6 - 4 - 5  15", "TotalBetValue": 7000, "RefundValue": 0, "PrizeValue": 0 }, { "GameSessionID": 713495, "StartTime": "2016-04-28T05:18:00", "LocationName": "Xá»‰u", "Result": "5 - 5 - 4  14", "TotalBetValue": 7000, "RefundValue": 7000, "PrizeValue": 0 }];
        //            LuckyDiceGame.BindHistory(tabRoom, current);
    }

    luckyDiceLogic.prototype.BindHistory = function (tabRoom, current) {
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.Url_Root + 'MiniGameLuckyDice/LuckyDiceHistory?tabRoom=' + tabRoom,
            success: function (data) {
                LuckyDiceGame.SetPopup(900, 448, data);

                var dataHistory = LuckyDiceGame.cacheData.slice((current - 1) * LuckyDiceGame.rowperPage);
                var totalPage = Math.ceil(LuckyDiceGame.cacheData.length / LuckyDiceGame.rowperPage);
                var stringHtml = '';
                var dataLength = 10;
                if (totalPage == current) dataLength = dataHistory.length;
                for (var i = 0; i < dataLength; i++) {
                    if (i % 2 != 0) stringHtml += '<tr class="tx_nen_noidung_bang_lichsu_giaodich">';
                    else stringHtml += '<tr>';
                    stringHtml += '<td>' + dataHistory[i].GameSessionID + '</td>';
                    stringHtml += '<td>' + LuckyDiceGame.formDateTimehms(dataHistory[i].StartTime) + '</td>';
                    stringHtml += '<td>' + dataHistory[i].LocationName + '</td>';
                    stringHtml += '<td>' + LuckyDiceGame.ReplaceStringHistory(dataHistory[i].Result) + '</td>';
                    stringHtml += '<td>' + LuckyDiceGame.FormatNumber(dataHistory[i].TotalBetValue) + '</td>';
                    stringHtml += '<td>' + LuckyDiceGame.FormatNumber(dataHistory[i].RefundValue) + '</td>';
                    stringHtml += '<td>' + LuckyDiceGame.FormatNumber(dataHistory[i].PrizeValue) + '</td>';
                    stringHtml += '</tr>';
                }
                $('#tx_table_listHistory').html(stringHtml);
                if (tabRoom == 1) $('#tx_table_listHistory').css('color', '#ffb72f');
                else $('#tx_table_listHistory').css('color', 'white');
                // PhĂ¢n trang history
                var stringListHistoryCurrent = '';
                if (current > 1) stringListHistoryCurrent += '<li><a href="javascript:;" onclick="LuckyDiceGame.ShowHistory(' + tabRoom + ',' + (current - 1) + ')"><<</a></li>';
                var pageCount = 0;
                var startPage = 0;
                if (totalPage == current) {
                    startPage = current - 1;
                } else if (totalPage - current < 3) {
                    if (current - 3 > 1) startPage = current - 3;
                    else startPage = 1;
                } else {
                    if (current - 2 > 1) startPage = current - 2;
                    else startPage = 1;
                }
                for (var i = startPage; i <= totalPage; i++) {
                    if (pageCount == 5) break;
                    if (i == current) stringListHistoryCurrent += '<li class="tx_active_bang"><a href="javascript:;" onclick="">' + i + '</a></li>';
                    else stringListHistoryCurrent += '<li><a href="javascript:;" onclick="LuckyDiceGame.ShowHistory(' + tabRoom + ',' + i + ')">' + i + '</a></li>';
                    pageCount++;
                }

                if (current != totalPage) stringListHistoryCurrent += '<li><a href="javascript:;" onclick="LuckyDiceGame.ShowHistory(' + tabRoom + ',' + (current + 1) + ')">>></a></li>';

                if (totalPage > 1) $('#tx_listHistory_current').html(stringListHistoryCurrent);
            },
            fail: function (fail) {
                console.log('loi nhe');
            }
        });
    }

    luckyDiceLogic.prototype.GetTop20 = function (currentGameSessionId) {
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.GetSessionDetailUrl + "GetTop20RecentSessions/?r=" + Math.random(),
            crossDomain: true,
            xhrFields: {
                withCredentials: true
            },
            success: function (data) {
                if (data.length > 0) {
                    LuckyDiceGame.top20Data = data;
                    LuckyDiceGame.GetDetailSession(currentGameSessionId, LuckyDiceGame.isRoom);
                }
            }
        });
    }

    luckyDiceLogic.prototype.ShowSessionId = function (roomOld, roomNew, currentGameSessionId) {
        if (roomOld == roomNew) {
            return;
        } else {
            LuckyDiceGame.GetDetailSession(currentGameSessionId, roomNew);
        }
    }

    luckyDiceLogic.prototype.GetDetailSession = function (currentGameSessionId, room) {
        var isOdd = -1;
        if (this.top20Data[0].IsOdd == true) {
            isOdd = 1;
        } else {
            isOdd = 0;
        }
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.GetSessionDetailUrl + "GetSessionDetailsTX?gameSessionId=" + currentGameSessionId + "&isOdd=" + isOdd + "&betType=" + room + "&r=" + Math.random(),

            xhrFields: {
                withCredentials: true
            },
            success: function (data) {
                if (data != null)
                    LuckyDiceGame.BindHistorySession(data, currentGameSessionId, room);
            }
        });
    }

    luckyDiceLogic.prototype.BindHistorySession = function (dataSesion, currentGameSessionId, room) {
        //dataSesion = { "SessionDetailsData": [{ "AccountID": 117122816, "Username": "cuyeuna***", "BetType": 1, "LocationID": 2, "BetValue": 444444, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.04" }, { "AccountID": 96631134, "Username": "tuanson***", "BetType": 1, "LocationID": 1, "BetValue": 1500, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.077" }, { "AccountID": 132385751, "Username": "pro_***", "BetType": 1, "LocationID": 2, "BetValue": 40000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.093" }, { "AccountID": 140992135, "Username": "id08111***", "BetType": 1, "LocationID": 1, "BetValue": 25000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.197" }, { "AccountID": 118793459, "Username": "kho***", "BetType": 1, "LocationID": 1, "BetValue": 20000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.22" }, { "AccountID": 1203205859, "Username": "0166612***", "BetType": 1, "LocationID": 2, "BetValue": 123698, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.39" }, { "AccountID": 1201728604, "Username": "tucon.6***", "BetType": 1, "LocationID": 1, "BetValue": 30000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.457" }, { "AccountID": 1204533103, "Username": "vudinha***", "BetType": 1, "LocationID": 1, "BetValue": 3000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.473" }, { "AccountID": 1204510915, "Username": "anhduc1***", "BetType": 1, "LocationID": 1, "BetValue": 7820, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.563" }, { "AccountID": 1202112558, "Username": "vtc.bet***", "BetType": 1, "LocationID": 1, "BetValue": 120000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.593" }, { "AccountID": 1204532964, "Username": "vtc2454***", "BetType": 1, "LocationID": 1, "BetValue": 5000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.62" }, { "AccountID": 1202368868, "Username": "memecom***", "BetType": 1, "LocationID": 2, "BetValue": 100000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.647" }, { "AccountID": 1204133421, "Username": "locdua2***", "BetType": 1, "LocationID": 2, "BetValue": 20000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.653" }, { "AccountID": 1204348216, "Username": "0901384***", "BetType": 1, "LocationID": 2, "BetValue": 9999, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.717" }, { "AccountID": 1203276396, "Username": "zxduykh***", "BetType": 1, "LocationID": 1, "BetValue": 200000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.817" }, { "AccountID": 1203132363, "Username": "truong1***", "BetType": 1, "LocationID": 1, "BetValue": 1000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.843" }, { "AccountID": 123140977, "Username": "sanbang***", "BetType": 1, "LocationID": 1, "BetValue": 9000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:30.96" }, { "AccountID": 1204439029, "Username": "redbull***", "BetType": 1, "LocationID": 1, "BetValue": 5000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.023" }, { "AccountID": 1204532800, "Username": "vkl.vtc***", "BetType": 1, "LocationID": 2, "BetValue": 25000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.053" }, { "AccountID": 119050128, "Username": "keu***", "BetType": 1, "LocationID": 1, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.093" }, { "AccountID": 134702891, "Username": "saohihi***", "BetType": 1, "LocationID": 1, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.14" }, { "AccountID": 110595541, "Username": "minhtru***", "BetType": 1, "LocationID": 2, "BetValue": 100000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.197" }, { "AccountID": 1203082597, "Username": "0167610***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.207" }, { "AccountID": 155602089, "Username": "hoaithu***", "BetType": 1, "LocationID": 2, "BetValue": 1200, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.32" }, { "AccountID": 1204084508, "Username": "aa01648***", "BetType": 1, "LocationID": 2, "BetValue": 41000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.523" }, { "AccountID": 154616102, "Username": "bibe2k1***", "BetType": 1, "LocationID": 2, "BetValue": 32000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.653" }, { "AccountID": 1204234542, "Username": "levanvi***", "BetType": 1, "LocationID": 1, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.717" }, { "AccountID": 1200394215, "Username": "bienlan***", "BetType": 1, "LocationID": 2, "BetValue": 100000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.873" }, { "AccountID": 1202816204, "Username": "ngocthu***", "BetType": 1, "LocationID": 2, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:31.977" }, { "AccountID": 1204176362, "Username": "phatloc***", "BetType": 1, "LocationID": 1, "BetValue": 5000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:32.4" }, { "AccountID": 151332503, "Username": "theboge***", "BetType": 1, "LocationID": 1, "BetValue": 30000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:32.673" }, { "AccountID": 1203479134, "Username": "duatien***", "BetType": 1, "LocationID": 1, "BetValue": 2000000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:32.753" }, { "AccountID": 110793727, "Username": "phihail***", "BetType": 1, "LocationID": 2, "BetValue": 5000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:32.8" }, { "AccountID": 1201380623, "Username": "syquan2***", "BetType": 1, "LocationID": 1, "BetValue": 40000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:32.993" }, { "AccountID": 1204197237, "Username": "votong1***", "BetType": 1, "LocationID": 2, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:33.4" }, { "AccountID": 150937883, "Username": "kun_***", "BetType": 1, "LocationID": 1, "BetValue": 22222, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:33.403" }, { "AccountID": 152699407, "Username": "0122201***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:33.67" }, { "AccountID": 155187303, "Username": "huykent***", "BetType": 1, "LocationID": 1, "BetValue": 7000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:34.333" }, { "AccountID": 149526114, "Username": "innova2***", "BetType": 1, "LocationID": 1, "BetValue": 275000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:34.38" }, { "AccountID": 1203479888, "Username": "bevandu***", "BetType": 1, "LocationID": 1, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:35.34" }, { "AccountID": 1204456596, "Username": "manhhun***", "BetType": 1, "LocationID": 2, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:35.647" }, { "AccountID": 142048075, "Username": "tuantom***", "BetType": 1, "LocationID": 2, "BetValue": 150000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:35.827" }, { "AccountID": 153520617, "Username": "hoaroic***", "BetType": 1, "LocationID": 2, "BetValue": 15555, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:36.09" }, { "AccountID": 153519266, "Username": "quanbeo***", "BetType": 1, "LocationID": 1, "BetValue": 25000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:36.093" }, { "AccountID": 1204532874, "Username": "quay.ta***", "BetType": 1, "LocationID": 2, "BetValue": 59999, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:36.133" }, { "AccountID": 155860377, "Username": "xincaiv***", "BetType": 1, "LocationID": 2, "BetValue": 2000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:36.177" }, { "AccountID": 1203160730, "Username": "bachim.***", "BetType": 1, "LocationID": 2, "BetValue": 3000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:36.243" }, { "AccountID": 154616102, "Username": "bibe2k1***", "BetType": 1, "LocationID": 2, "BetValue": 1920, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:36.313" }, { "AccountID": 1200932003, "Username": "tanl***", "BetType": 1, "LocationID": 1, "BetValue": 1000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:36.333" }, { "AccountID": 154221263, "Username": "juni.10***", "BetType": 1, "LocationID": 1, "BetValue": 5700, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:36.463" }, { "AccountID": 151795454, "Username": "hunghb9***", "BetType": 1, "LocationID": 2, "BetValue": 15000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:36.667" }, { "AccountID": 1202662858, "Username": "coibipb***", "BetType": 1, "LocationID": 2, "BetValue": 5000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:36.98" }, { "AccountID": 1203330259, "Username": "bananaa***", "BetType": 1, "LocationID": 1, "BetValue": 400000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:37.227" }, { "AccountID": 1201457908, "Username": "canabis***", "BetType": 1, "LocationID": 2, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:37.397" }, { "AccountID": 144250210, "Username": "rurutyt***", "BetType": 1, "LocationID": 2, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:37.413" }, { "AccountID": 1204134790, "Username": "susu090***", "BetType": 1, "LocationID": 2, "BetValue": 6000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:37.44" }, { "AccountID": 124134921, "Username": "yeuphuo***", "BetType": 1, "LocationID": 1, "BetValue": 8000000, "RefundValue": 7427940, "CreatedTime": "2016-06-02T03:58:37.553" }, { "AccountID": 1201728604, "Username": "tucon.6***", "BetType": 1, "LocationID": 1, "BetValue": 4608, "RefundValue": 4608, "CreatedTime": "2016-06-02T03:58:37.76" }, { "AccountID": 1203231867, "Username": "xinhbon***", "BetType": 1, "LocationID": 1, "BetValue": 24000, "RefundValue": 24000, "CreatedTime": "2016-06-02T03:58:37.77" }, { "AccountID": 154993507, "Username": "cadaph1***", "BetType": 1, "LocationID": 1, "BetValue": 57082, "RefundValue": 57082, "CreatedTime": "2016-06-02T03:58:38.043" }, { "AccountID": 125726180, "Username": "0973776***", "BetType": 1, "LocationID": 2, "BetValue": 100000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:38.507" }, { "AccountID": 151332503, "Username": "theboge***", "BetType": 1, "LocationID": 1, "BetValue": 14491, "RefundValue": 14491, "CreatedTime": "2016-06-02T03:58:38.717" }, { "AccountID": 1203155021, "Username": "ntgiap0***", "BetType": 1, "LocationID": 2, "BetValue": 7500, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:39.043" }, { "AccountID": 1201773366, "Username": "noquykh***", "BetType": 1, "LocationID": 2, "BetValue": 24000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:39.147" }, { "AccountID": 1204533222, "Username": "toiloi.***", "BetType": 1, "LocationID": 2, "BetValue": 2450, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:39.283" }, { "AccountID": 1201260572, "Username": "bao2014***", "BetType": 1, "LocationID": 1, "BetValue": 22222, "RefundValue": 22222, "CreatedTime": "2016-06-02T03:58:39.327" }, { "AccountID": 132750535, "Username": "0944609***", "BetType": 1, "LocationID": 2, "BetValue": 43566, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:39.637" }, { "AccountID": 141589248, "Username": "pm.cole***", "BetType": 1, "LocationID": 1, "BetValue": 6864, "RefundValue": 6864, "CreatedTime": "2016-06-02T03:58:40.743" }, { "AccountID": 1201457908, "Username": "canabis***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:41.213" }, { "AccountID": 1201116782, "Username": "adidasm***", "BetType": 1, "LocationID": 1, "BetValue": 8000, "RefundValue": 8000, "CreatedTime": "2016-06-02T03:58:41.653" }, { "AccountID": 152902892, "Username": "thuydun***", "BetType": 1, "LocationID": 2, "BetValue": 4000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:42.123" }, { "AccountID": 152945119, "Username": "lasaoph***", "BetType": 1, "LocationID": 1, "BetValue": 30000, "RefundValue": 30000, "CreatedTime": "2016-06-02T03:58:42.233" }, { "AccountID": 124134921, "Username": "yeuphuo***", "BetType": 1, "LocationID": 1, "BetValue": 950661, "RefundValue": 950661, "CreatedTime": "2016-06-02T03:58:42.42" }, { "AccountID": 143541571, "Username": "nghia99***", "BetType": 1, "LocationID": 2, "BetValue": 15000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:43.06" }, { "AccountID": 1201773366, "Username": "noquykh***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:43.313" }, { "AccountID": 125488328, "Username": "lequang***", "BetType": 1, "LocationID": 2, "BetValue": 500000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:43.503" }, { "AccountID": 151332503, "Username": "theboge***", "BetType": 1, "LocationID": 1, "BetValue": 9910, "RefundValue": 9910, "CreatedTime": "2016-06-02T03:58:43.97" }, { "AccountID": 126458059, "Username": "danglap***", "BetType": 1, "LocationID": 2, "BetValue": 3864, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:44.02" }, { "AccountID": 136935669, "Username": "0126414***", "BetType": 1, "LocationID": 1, "BetValue": 5000, "RefundValue": 5000, "CreatedTime": "2016-06-02T03:58:44.32" }, { "AccountID": 1203021931, "Username": "chjchu0***", "BetType": 1, "LocationID": 2, "BetValue": 28182, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:44.713" }, { "AccountID": 1204456596, "Username": "manhhun***", "BetType": 1, "LocationID": 2, "BetValue": 40000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:44.723" }, { "AccountID": 1203231867, "Username": "xinhbon***", "BetType": 1, "LocationID": 1, "BetValue": 754, "RefundValue": 754, "CreatedTime": "2016-06-02T03:58:45.633" }, { "AccountID": 1204497440, "Username": "luckey2***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:46.717" }, { "AccountID": 150544545, "Username": "phucl0v***", "BetType": 1, "LocationID": 1, "BetValue": 6000, "RefundValue": 6000, "CreatedTime": "2016-06-02T03:58:49.22" }, { "AccountID": 1201808100, "Username": "nhoc.s2***", "BetType": 1, "LocationID": 2, "BetValue": 30000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:49.273" }, { "AccountID": 1203231867, "Username": "xinhbon***", "BetType": 1, "LocationID": 1, "BetValue": 3000, "RefundValue": 3000, "CreatedTime": "2016-06-02T03:58:49.54" }, { "AccountID": 126001714, "Username": "kgemanh***", "BetType": 1, "LocationID": 2, "BetValue": 1725, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:49.57" }, { "AccountID": 1204532895, "Username": "vkngoc8***", "BetType": 1, "LocationID": 2, "BetValue": 15000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:50.13" }, { "AccountID": 139310610, "Username": "nf4e***", "BetType": 1, "LocationID": 2, "BetValue": 20000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:50.2" }, { "AccountID": 150177884, "Username": "halfbri***", "BetType": 1, "LocationID": 1, "BetValue": 1000, "RefundValue": 1000, "CreatedTime": "2016-06-02T03:58:50.24" }, { "AccountID": 129365885, "Username": "0969668***", "BetType": 1, "LocationID": 1, "BetValue": 276, "RefundValue": 276, "CreatedTime": "2016-06-02T03:58:50.69" }, { "AccountID": 150474663, "Username": "dngoc.l***", "BetType": 1, "LocationID": 1, "BetValue": 150000, "RefundValue": 150000, "CreatedTime": "2016-06-02T03:58:50.873" }, { "AccountID": 1204294703, "Username": "cuongin***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:51.513" }, { "AccountID": 1202196972, "Username": "tuanvay***", "BetType": 1, "LocationID": 1, "BetValue": 15000, "RefundValue": 15000, "CreatedTime": "2016-06-02T03:58:52.353" }, { "AccountID": 1204482485, "Username": "datsake***", "BetType": 1, "LocationID": 1, "BetValue": 3000, "RefundValue": 3000, "CreatedTime": "2016-06-02T03:58:52.68" }, { "AccountID": 1202468987, "Username": "labaidi***", "BetType": 1, "LocationID": 2, "BetValue": 200000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:53.507" }, { "AccountID": 1203148049, "Username": "chuoima***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:54.04" }, { "AccountID": 1204087156, "Username": "0121638***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:54.16" }, { "AccountID": 148525322, "Username": "kin0410***", "BetType": 1, "LocationID": 2, "BetValue": 220079, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:54.313" }, { "AccountID": 1203166659, "Username": "bomb***", "BetType": 1, "LocationID": 2, "BetValue": 100000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:54.583" }, { "AccountID": 151720032, "Username": "vtcid91***", "BetType": 1, "LocationID": 2, "BetValue": 12000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:55.13" }, { "AccountID": 153608927, "Username": "choithu***", "BetType": 1, "LocationID": 2, "BetValue": 16194, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:55.47" }, { "AccountID": 1201521939, "Username": "dungga9***", "BetType": 1, "LocationID": 2, "BetValue": 4999, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:55.603" }, { "AccountID": 1203851981, "Username": "roct***", "BetType": 1, "LocationID": 2, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:56.01" }, { "AccountID": 1204456596, "Username": "manhhun***", "BetType": 1, "LocationID": 2, "BetValue": 29741, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:56.163" }, { "AccountID": 1202196972, "Username": "tuanvay***", "BetType": 1, "LocationID": 1, "BetValue": 15000, "RefundValue": 15000, "CreatedTime": "2016-06-02T03:58:56.25" }, { "AccountID": 121783534, "Username": "vtcid05***", "BetType": 1, "LocationID": 2, "BetValue": 30000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:56.783" }, { "AccountID": 1204532895, "Username": "vkngoc8***", "BetType": 1, "LocationID": 2, "BetValue": 560, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:57.1" }, { "AccountID": 150295004, "Username": "kutrung***", "BetType": 1, "LocationID": 2, "BetValue": 1500, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:57.567" }, { "AccountID": 1204531767, "Username": "zmeo***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:58.047" }, { "AccountID": 1201412340, "Username": "0916077***", "BetType": 1, "LocationID": 2, "BetValue": 2000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:58.347" }, { "AccountID": 153609163, "Username": "nguyenn***", "BetType": 1, "LocationID": 2, "BetValue": 2000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:58:59.677" }, { "AccountID": 141704115, "Username": "taonguy***", "BetType": 1, "LocationID": 1, "BetValue": 500000, "RefundValue": 500000, "CreatedTime": "2016-06-02T03:59:00.57" }, { "AccountID": 144896281, "Username": "phoenix***", "BetType": 1, "LocationID": 2, "BetValue": 5000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:03.013" }, { "AccountID": 1202112558, "Username": "vtc.bet***", "BetType": 1, "LocationID": 1, "BetValue": 40000, "RefundValue": 40000, "CreatedTime": "2016-06-02T03:59:03.09" }, { "AccountID": 141589248, "Username": "pm.cole***", "BetType": 1, "LocationID": 1, "BetValue": 300, "RefundValue": 300, "CreatedTime": "2016-06-02T03:59:03.183" }, { "AccountID": 118793459, "Username": "kho***", "BetType": 1, "LocationID": 1, "BetValue": 10000, "RefundValue": 10000, "CreatedTime": "2016-06-02T03:59:03.827" }, { "AccountID": 1203851981, "Username": "roct***", "BetType": 1, "LocationID": 2, "BetValue": 10012, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:05.84" }, { "AccountID": 140790833, "Username": "hunglam***", "BetType": 1, "LocationID": 2, "BetValue": 12000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:06.273" }, { "AccountID": 152902892, "Username": "thuydun***", "BetType": 1, "LocationID": 2, "BetValue": 5000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:06.847" }, { "AccountID": 1203783979, "Username": "tutoan7***", "BetType": 1, "LocationID": 1, "BetValue": 750, "RefundValue": 750, "CreatedTime": "2016-06-02T03:59:07.123" }, { "AccountID": 138794493, "Username": "buong_x***", "BetType": 1, "LocationID": 2, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:08.373" }, { "AccountID": 1202235455, "Username": "hoangvy***", "BetType": 1, "LocationID": 2, "BetValue": 5000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:08.63" }, { "AccountID": 1204292431, "Username": "luanhie***", "BetType": 1, "LocationID": 2, "BetValue": 4145, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:08.867" }, { "AccountID": 1203934742, "Username": "thiendi***", "BetType": 1, "LocationID": 2, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:09.06" }, { "AccountID": 1204531616, "Username": "mobifon***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:09.067" }, { "AccountID": 1203851981, "Username": "roct***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:09.17" }, { "AccountID": 141589248, "Username": "pm.cole***", "BetType": 1, "LocationID": 1, "BetValue": 600, "RefundValue": 600, "CreatedTime": "2016-06-02T03:59:09.3" }, { "AccountID": 1201521939, "Username": "dungga9***", "BetType": 1, "LocationID": 2, "BetValue": 5000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:09.593" }, { "AccountID": 1204015641, "Username": "tunganh***", "BetType": 1, "LocationID": 1, "BetValue": 30000, "RefundValue": 30000, "CreatedTime": "2016-06-02T03:59:09.673" }, { "AccountID": 1202384798, "Username": "0923096***", "BetType": 1, "LocationID": 2, "BetValue": 15000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:09.953" }, { "AccountID": 1203769496, "Username": "nhoxbin***", "BetType": 1, "LocationID": 2, "BetValue": 1282, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:10.103" }, { "AccountID": 1203722063, "Username": "nhoconb***", "BetType": 1, "LocationID": 2, "BetValue": 50, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:10.83" }, { "AccountID": 127447556, "Username": "conan19***", "BetType": 1, "LocationID": 2, "BetValue": 200000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:10.967" }, { "AccountID": 1204407089, "Username": "nguyenk***", "BetType": 1, "LocationID": 1, "BetValue": 2000, "RefundValue": 2000, "CreatedTime": "2016-06-02T03:59:11.01" }, { "AccountID": 154897898, "Username": "cadaph1***", "BetType": 1, "LocationID": 1, "BetValue": 87110, "RefundValue": 87110, "CreatedTime": "2016-06-02T03:59:14.09" }, { "AccountID": 1203689942, "Username": "canhbe1***", "BetType": 1, "LocationID": 2, "BetValue": 5000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:14.127" }, { "AccountID": 1204273849, "Username": "vtc.id0***", "BetType": 1, "LocationID": 2, "BetValue": 40000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:14.813" }, { "AccountID": 131784333, "Username": "h.i.3.u***", "BetType": 1, "LocationID": 1, "BetValue": 2500, "RefundValue": 2500, "CreatedTime": "2016-06-02T03:59:15.41" }, { "AccountID": 1202640273, "Username": "c26.08.***", "BetType": 1, "LocationID": 2, "BetValue": 15000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:15.913" }, { "AccountID": 141589248, "Username": "pm.cole***", "BetType": 1, "LocationID": 1, "BetValue": 36, "RefundValue": 36, "CreatedTime": "2016-06-02T03:59:16.12" }, { "AccountID": 50898140, "Username": "xuanoan***", "BetType": 1, "LocationID": 1, "BetValue": 2000, "RefundValue": 2000, "CreatedTime": "2016-06-02T03:59:16.39" }, { "AccountID": 1204197237, "Username": "votong1***", "BetType": 1, "LocationID": 2, "BetValue": 20000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:17.08" }, { "AccountID": 110793727, "Username": "phihail***", "BetType": 1, "LocationID": 2, "BetValue": 760, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:17.28" }, { "AccountID": 131784333, "Username": "h.i.3.u***", "BetType": 1, "LocationID": 1, "BetValue": 5000, "RefundValue": 5000, "CreatedTime": "2016-06-02T03:59:17.657" }, { "AccountID": 153285659, "Username": "0915402***", "BetType": 1, "LocationID": 2, "BetValue": 11669, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:17.703" }, { "AccountID": 150544545, "Username": "phucl0v***", "BetType": 1, "LocationID": 1, "BetValue": 4000, "RefundValue": 4000, "CreatedTime": "2016-06-02T03:59:18.17" }, { "AccountID": 152699407, "Username": "0122201***", "BetType": 1, "LocationID": 2, "BetValue": 5000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:18.213" }, { "AccountID": 151720032, "Username": "vtcid91***", "BetType": 1, "LocationID": 2, "BetValue": 1321, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:18.253" }, { "AccountID": 1203082597, "Username": "0167610***", "BetType": 1, "LocationID": 2, "BetValue": 2000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:18.54" }, { "AccountID": 121783534, "Username": "vtcid05***", "BetType": 1, "LocationID": 2, "BetValue": 2000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:18.563" }, { "AccountID": 1203380247, "Username": "kiepvua***", "BetType": 1, "LocationID": 2, "BetValue": 20000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:18.933" }, { "AccountID": 1204234542, "Username": "levanvi***", "BetType": 1, "LocationID": 1, "BetValue": 50000, "RefundValue": 50000, "CreatedTime": "2016-06-02T03:59:19.343" }, { "AccountID": 1204427251, "Username": "id12345***", "BetType": 1, "LocationID": 2, "BetValue": 7561, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:19.387" }, { "AccountID": 1203180376, "Username": "xuyenng***", "BetType": 1, "LocationID": 2, "BetValue": 100000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:19.593" }, { "AccountID": 148589453, "Username": "hoangth***", "BetType": 1, "LocationID": 2, "BetValue": 10084, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:19.943" }, { "AccountID": 132750535, "Username": "0944609***", "BetType": 1, "LocationID": 2, "BetValue": 7531, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:20.583" }, { "AccountID": 1204532823, "Username": "viettel***", "BetType": 1, "LocationID": 2, "BetValue": 7000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:20.837" }, { "AccountID": 1201644385, "Username": "0908926***", "BetType": 1, "LocationID": 2, "BetValue": 25929, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:22.223" }, { "AccountID": 1201728904, "Username": "laytroi***", "BetType": 1, "LocationID": 2, "BetValue": 50000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:22.253" }, { "AccountID": 153285659, "Username": "0915402***", "BetType": 1, "LocationID": 2, "BetValue": 120, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:22.26" }, { "AccountID": 121783534, "Username": "vtcid05***", "BetType": 1, "LocationID": 2, "BetValue": 18000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:22.287" }, { "AccountID": 141589248, "Username": "pm.cole***", "BetType": 1, "LocationID": 1, "BetValue": 199, "RefundValue": 199, "CreatedTime": "2016-06-02T03:59:22.43" }, { "AccountID": 1204529921, "Username": "toan.19***", "BetType": 1, "LocationID": 2, "BetValue": 299, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:22.497" }, { "AccountID": 123966542, "Username": "phongkh***", "BetType": 1, "LocationID": 2, "BetValue": 5889, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:22.697" }, { "AccountID": 1203790712, "Username": "hopbacn***", "BetType": 1, "LocationID": 1, "BetValue": 1000, "RefundValue": 1000, "CreatedTime": "2016-06-02T03:59:22.787" }, { "AccountID": 1204333035, "Username": "trungni***", "BetType": 1, "LocationID": 2, "BetValue": 4500, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:22.807" }, { "AccountID": 1204532413, "Username": "lanhuon***", "BetType": 1, "LocationID": 2, "BetValue": 2000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:23.103" }, { "AccountID": 148917620, "Username": "kiemlin***", "BetType": 1, "LocationID": 2, "BetValue": 15000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:23.513" }, { "AccountID": 1203689942, "Username": "canhbe1***", "BetType": 1, "LocationID": 2, "BetValue": 2000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:23.54" }, { "AccountID": 1204292431, "Username": "luanhie***", "BetType": 1, "LocationID": 2, "BetValue": 935, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:24.4" }, { "AccountID": 1202002009, "Username": "denthen***", "BetType": 1, "LocationID": 2, "BetValue": 22000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:24.76" }, { "AccountID": 1203934742, "Username": "thiendi***", "BetType": 1, "LocationID": 2, "BetValue": 20000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:24.943" }, { "AccountID": 151720032, "Username": "vtcid91***", "BetType": 1, "LocationID": 2, "BetValue": 10000, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:25.04" }, { "AccountID": 128651831, "Username": "ngao.op***", "BetType": 1, "LocationID": 2, "BetValue": 11040, "RefundValue": 0, "CreatedTime": "2016-06-02T03:59:29" }], "location": 1, "dice1": 5, "dice2": 3, "dice3": 2, "diceResult": 10, "Date": "02/06/2016" };
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.Url_Root + 'MiniGameLuckyDice/LuckyDicePhien?tabRoom=' + room + '&currentGameSessionId=' + currentGameSessionId,
            success: function (data) {
                LuckyDiceGame.SetPopup(780, 448, data);

                var arrdata = dataSesion.SessionDetailsData;
                var sumbet1 = 0, sumre1 = 0, sumbet2 = 0, sumre2 = 0;// tong tien bet, tra lai
                var string01 = '';
                var string02 = '';
                for (var i = 0; i < arrdata.length; i++) {
                    var string = '';

                    if (arrdata[i].LocationID == 2) {
                        string += '<tr>';
                        string += '<td>' + LuckyDiceGame.TDFormatDateTimeHMSZ(arrdata[i].CreatedTime) + '</td>';
                        string += '<td>' + arrdata[i].Username + '</td>';
                        string += '<td>' + LuckyDiceGame.FormatNumber(arrdata[i].RefundValue) + '</td>';
                        string += '<td>' + LuckyDiceGame.FormatNumber(arrdata[i].BetValue) + '</td>';
                        string += '</tr>';
                        sumbet2 += arrdata[i].BetValue;
                        sumre2 += arrdata[i].RefundValue;
                        string02 += string;
                    } else {
                        string += '<tr>';
                        string += '<td>' + LuckyDiceGame.FormatNumber(arrdata[i].BetValue) + '</td>';
                        string += '<td>' + LuckyDiceGame.FormatNumber(arrdata[i].RefundValue) + '</td>';
                        string += '<td>' + arrdata[i].Username + '</td>';
                        string += '<td>' + LuckyDiceGame.TDFormatDateTimeHMSZ(arrdata[i].CreatedTime) + '</td>';
                        string += '</tr>';
                        sumbet1 += arrdata[i].BetValue;
                        sumre1 += arrdata[i].RefundValue;
                        string01 += string;
                    }
                }
                $('#tx_sumbet1').html(LuckyDiceGame.FormatNumber(sumbet1));
                $('#tx_sumre1').html(LuckyDiceGame.FormatNumber(sumre1));
                $('#tx_sumbet2').html(LuckyDiceGame.FormatNumber(sumbet2));
                $('#tx_sumre2').html(LuckyDiceGame.FormatNumber(sumre2));

                $('#tx_tablelist02').html(string02);
                $('#tx_tablelist01').html(string01);

                if (room == 1) {
                    $('#tx_tablelist02').css('color', '#ffb72f');
                    $('#tx_tablelist01').css('color', '#ffb72f');
                } else {
                    $('#tx_tablelist02').css('color', 'white');
                    $('#tx_tablelist01').css('color', 'white');
                }
                var stringDiem = '';
                if (currentGameSessionId == LuckyDiceGame.currentSession.GameSessionID) {
                    stringDiem = '';
                } else {
                    if (dataSesion.diceResult > 10) {
                        stringDiem = '<li class="animated infinite pulse"><img src="' + luckyDiceConfig.Url_Root + 'images/text_tai.png" alt=""></li>';
                        stringDiem += '<li class="tx_phien_bg_dice"><img src="' + luckyDiceConfig.Url_Root + 'images/result_' + dataSesion.dice1 + '.png" alt=""></li>';
                        stringDiem += '<li class="tx_phien_bg_dice"><img src="' + luckyDiceConfig.Url_Root + 'images/result_' + dataSesion.dice2 + '.png" alt=""></li>';
                        stringDiem += '<li  class="tx_phien_bg_dice"><img src="' + luckyDiceConfig.Url_Root + 'images/result_' + dataSesion.dice3 + '.png" alt=""></li>';
                        stringDiem += '<li>' + dataSesion.diceResult + '</li>';
                        stringDiem += '<li class="infinite pulse"><img src="' + luckyDiceConfig.Url_Root + 'images/text_xiu.png" alt=""></li>';
                    } else {
                        stringDiem = '<li class="infinite pulse"><img src="' + luckyDiceConfig.Url_Root + 'images/text_tai.png" alt=""></li>';
                        stringDiem += '<li class="tx_phien_bg_dice"><img src="' + luckyDiceConfig.Url_Root + 'images/result_' + dataSesion.dice1 + '.png" alt=""></li>';
                        stringDiem += '<li class="tx_phien_bg_dice"><img src="' + luckyDiceConfig.Url_Root + 'images/result_' + dataSesion.dice2 + '.png" alt=""></li>';
                        stringDiem += '<li  class="tx_phien_bg_dice"><img src="' + luckyDiceConfig.Url_Root + 'images/result_' + dataSesion.dice3 + '.png" alt=""></li>';
                        stringDiem += '<li>' + dataSesion.diceResult + '</li>';
                        stringDiem += '<li class="animated infinite pulse"><img src="' + luckyDiceConfig.Url_Root + 'images/text_xiu.png" alt=""></li>';
                    }
                }

                $('#tx_session_diem').html(stringDiem);

                $('#tx_session_time').html('phiĂªn <i class="tx_mau_phien_taixiu">' + currentGameSessionId + '</i> ngĂ y ' + dataSesion.Date);

                $('#tx_all_table_phien').mCustomScrollbar({ autoHideScrollbar: true, advanced: { updateOnContentResize: true } });
                //$('#listPhien01').mCustomScrollbar({ autoHideScrollbar: true, advanced: { updateOnContentResize: true } });
            },
            fail: function (fail) {
                console.log('loi nhe');
            }
        });
    }

    luckyDiceLogic.prototype.NextSession = function (currentGameSessionId) {
        var checkSessionId = false;
        for (var i = 0; i < this.top20Data.length; i++) {
            if (this.top20Data[i].GameSessionID == currentGameSessionId) checkSessionId = true;
        }

        if (checkSessionId) this.GetTop20(currentGameSessionId);
        else return;
    }

    luckyDiceLogic.prototype.ShowTanLoc = function () {
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.Url_Root + 'MiniGameLuckyDice/LuckyDiceTanLoc',
            success: function (data) {
                LuckyDiceGame.SetPopup(480, 315, data);

            },
            fail: function (fail) {
                console.log('loi nhe');
            }
        });
    }

    luckyDiceLogic.prototype.LoadHtml = function () {
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.Url_Root + 'MiniGameLuckyDice/MainLukyDice',
            success: function (data) {
                $('body').append(data);
                $('#allGameLuckyDice').draggable();
                $('#tx_bat_nan').draggable();
                LuckyDiceGame.LoadCanvas();
				// //Load thong tin event
				// EventTX2016T5.GetAccountInfo();
				// EventTX2016T5.GetEventTime();

                $("#taixiuHeaderGame img").unbind("click");
                $("#taixiuHeaderGame img").bind("click", function () {
                    LuckyDiceGame.ShowHideLuckyDice();
                });

                //$(document).tooltip();
            },
            fail: function (fail) {
                console.log('loi nhe');
            }
        });
    }

    luckyDiceLogic.prototype.SelectEffect = function () {
        if (this.isEffect) {
            this.isEffect = false;
            $('#tx_type_effect').removeClass('tx_nen_btn01');
            $('#tx_type_effect').addClass('tx_nen_btn02');
        } else {
            this.isEffect = true;
            $('#tx_type_effect').removeClass('tx_nen_btn02');
            $('#tx_type_effect').addClass('tx_nen_btn01');
        }
    }

    luckyDiceLogic.prototype.LoadCanvas = function () {
        this.tickWait = 30;
        this.tickBet = 60;
        this.isEffect = false;
        this.isMoneyResult = true;
        var that = this;

        var canvasimg = document.getElementById('canvasTX');
        this.stageCanvas = new createjs.Stage(canvasimg);
        this.stageCanvas.enableMouseOver(30);
        this.stageCanvas.mouseEnabled = true;
        createjs.Touch.enable(this.stageCanvas);
        this.stageCanvas.mouseMoveOutside = true;
        createjs.Ticker.setFPS(30);
        createjs.Ticker.addEventListener('tick', function () {
            that.stageCanvas.update();
        });

        var bitmap = new createjs.Bitmap(this.loadResources.getResult('bg_xucxac'));
        bitmap.set({ alpha: 0 });

        this.textTime = new createjs.Text("00:00", "bold 24px Arial, Helvetica, sans-serif", "#ffc600");
        this.textTime.set({ x: 36, y: 53 });

        this.bg_bitmap = new createjs.Bitmap(this.loadResources.getResult('red_bg'));
        this.bg_bitmap.set({ x: 67, y: 67, regX: this.bg_bitmap.getBounds().width / 2, regY: this.bg_bitmap.getBounds().height / 2 });

        this.containerResult = new createjs.Container();

        this.stageCanvas.addChild(this.bg_bitmap, bitmap, this.textTime, this.containerResult);

        this.RunTimerTX();
        setInterval(that.RunTimerTX, 1000);

        this.GetVinhDanhTanLocMarquee();
        setInterval(that.GetVinhDanhTanLocMarquee, 180000);

        this.GetPointRutLoc();
        if (LuckyDiceGame.intevalGetPointTl) {
            clearInterval(LuckyDiceGame.intevalGetPointTl);
        }
        LuckyDiceGame.intevalGetPointTl = setInterval(function () {
            LuckyDiceGame.GetPointRutLoc();
        }, 90000);


        setInterval(function () {
            LuckyDiceGame.gameLuckyDiceHub.server.getCurrentRooms(LuckyDiceGame.isRoom).done(function () { }).fail();
        }, 30000);


        LuckydiceChat.StartChatTX();
        $('#tx_box_chat_all').css('display', 'block');
        setTimeout(function () {
            LuckydiceChat.RegisterChat();
        }, 3000);

    }

    luckyDiceLogic.prototype.StartEffectOpenBowl = function (callback) {
        $('#tx_bat_nan').css('top', '31px');
        $('#tx_bat_nan').css('left', '161px');
        $('#tx_bat_nan').show();
        callback();
    }

    luckyDiceLogic.prototype.StopEffectOpenBowl = function () {
        $('#tx_bat_nan').hide();
        $('#tx_bat_nan').css('top', '31px');
        $('#tx_bat_nan').css('left', '161px');
        this.LastResult();
    }

    luckyDiceLogic.prototype.CheckShowInTime = function () {
        if (this.tickWait > 0) {
            $('#totalDiemPhien').hide();
            this.stageCanvas.getChildAt(1).alpha = 1;
            this.bg_bitmap.alpha = 0;
            this.textTime.alpha = 0;
            this.containerResult.removeAllChildren();
            this.ShowDice(true);
        }
    }

    luckyDiceLogic.prototype.LoadResources = function () {
        var loadManifet = [
            { src: luckyDiceConfig.Url_Root + 'Content/taixiu.css' + luckyDiceLoaderVer },
            { src: luckyDiceConfig.Url_Root + 'Scripts/MiniGameLuckDice/chatLuckyDice.js' + luckyDiceLoaderVer }
        ];

        var loadManifet02 = [
            { src: luckyDiceConfig.Url_Root + 'images/xucxacEffect.png' + luckyDiceLoaderVer, id: "xucxacEffect" },
            { src: luckyDiceConfig.Url_Root + 'images/bg_xucxac.png' + luckyDiceLoaderVer, id: "bg_xucxac" },
            { src: luckyDiceConfig.Url_Root + 'images/result_xucxac.png' + luckyDiceLoaderVer, id: "result_xucxac" },
            { src: luckyDiceConfig.Url_Root + 'images/tx_bat_mo.png' + luckyDiceLoaderVer, id: "tx_bat_mo" },
            { src: luckyDiceConfig.Url_Root + 'images/red_bg.png' + luckyDiceLoaderVer, id: "red_bg" },
            { src: luckyDiceConfig.Url_Root + 'images/tx_bat1.png' + luckyDiceLoaderVer, id: "tx_bat1" },
            { src: luckyDiceConfig.Url_Root + 'images/tx_bat2.png' + luckyDiceLoaderVer, id: "tx_bat2" }
        ];

        this.loadResources = new createjs.LoadQueue();
        this.loadResources.on("complete", this.LoadHtml);
        this.loadResources.loadManifest(loadManifet);
        this.loadResources.loadManifest(loadManifet02);

    }

    luckyDiceLogic.prototype.AddMoneyTanLoc = function (money) {
        if ($('#moneyTanLoc').val().length > 0) {
            var inputMoney = $('#moneyTanLoc').val();
            inputMoney = parseInt(inputMoney.replace(/\./g, ''));
            $('#moneyTanLoc').val(LuckyDiceGame.FormatNumber(inputMoney + money));
        } else {
            $('#moneyTanLoc').val(LuckyDiceGame.FormatNumber(money));
        }
    }

    luckyDiceLogic.prototype.FormatMoneyNowTanLoc = function () {
        var inputMoney = $('#moneyTanLoc').val();
        inputMoney = parseInt(inputMoney.replace(/\./g, ''));
        if (inputMoney > 0) {
            $('#moneyTanLoc').val(LuckyDiceGame.FormatNumber(inputMoney));
        } else {
            $('#moneyTanLoc').val(0);
        }
    }

    luckyDiceLogic.prototype.TanLoc = function () {
        var inputMoney = $('#moneyTanLoc').val();
        inputMoney = parseInt(inputMoney.replace(/\./g, ''));
        if (inputMoney > 0) {
            $.ajax({
                type: "GET",
                url: luckyDiceConfig.Api_call_TanLoc + inputMoney,
                crossDomain: true,
                xhrFields: {
                    withCredentials: true
                },
                success: function (data) {
                    $('#moneyTanLoc').val('');
                    if (data.Respone > 0) {
                        $('#tx_tanloc_erro').html('Cáº£m Æ¡n báº¡n Ä‘Ă£ tĂ¡n lá»™c thĂ nh cĂ´ng! ChĂºc báº¡n gáº·p nhiá»u may máº¯n');
                        $('#tx_tanloc_erro').css('color', '#00FFA3');
                        $('#tx_tanloc_erro').css('display', 'block');
                        $(".sao-number p").html(LuckyDiceGame.FormatNumber(data.Balance));
                    } else {
                        if (data.Respone == -51) {
                            $('#tx_tanloc_erro').html('Báº¡n khĂ´ng Ä‘á»§ tiá»n Ä‘á»ƒ tĂ¡n lá»™c');
                            $('#tx_tanloc_erro').css('color', 'red');
                            $('#tx_tanloc_erro').css('display', 'block');
                        } else {
                            $('#tx_tanloc_erro').html('TĂ¡n lá»™c khĂ´ng thĂ nh cĂ´ng! Xin vui lĂ²ng thá»­ láº¡i');
                            $('#tx_tanloc_erro').css('color', 'red');
                            $('#tx_tanloc_erro').css('display', 'block');
                        }
                    }
                }
            });
        } else {
            $('#tx_tanloc_erro').html('Báº¡n nháº­p sá»‘ tiá»n tĂ¡n lá»™c chÆ°a chĂ­nh xĂ¡c! Nháº­p láº¡i');
            $('#tx_tanloc_erro').css('color', 'red');
            $('#tx_tanloc_erro').css('display', 'block');
        }
    }

    luckyDiceLogic.prototype.SelectRoom = function (room) {
        if (this.isRoom == room) {
            return;
        } else {
            this.CheckShowInTime();
            this.isRoom = room;
            $("#input_xiu_money").val('');
            $("#input_tai_money").val('');
            if (room == 1) {
                $('#tx_btn_roomSao').addClass('tx_btn_sao');
                $('#tx_btn_roomSao').removeClass('tx_btn_sao2');

                $('#tx_btn_roomXu').addClass('tx_btn_vang2');
                $('#tx_btn_roomXu').removeClass('tx_btn_vang');

                $('#mainTX').removeClass('tx_banxu');

            } else {
                $('#tx_btn_roomSao').addClass('tx_btn_sao2');
                $('#tx_btn_roomSao').removeClass('tx_btn_sao');

                $('#tx_btn_roomXu').addClass('tx_btn_vang');
                $('#tx_btn_roomXu').removeClass('tx_btn_vang2');

                $('#mainTX').addClass('tx_banxu');
            }
            try {
                LuckyDiceGame.gameLuckyDiceHub.server.getCurrentRooms(LuckyDiceGame.isRoom).done(function () { }).fail();
            } catch (e) { }
        }
    }

    luckyDiceLogic.prototype.ShowStatus = function (type, status) {
        if (type == 1 || type == 3) {
            if (type == 1) $('#tx_game_erro').css('color', 'red');
            else $('#tx_game_erro').css('color', '#00FFA3');

            $('#listSoiCauTX').hide();
            $('#tx_game_erro').show();
            $('#tx_game_erro').html(status);

            setTimeout(function () {
                $('#tx_game_erro').css('color', 'red');
                $('#listSoiCauTX').show();
                $('#tx_game_erro').hide();
            }, 2000);
        } else if (type == 2) {
            $('#tx_game_erro').show();
            $('#tx_game_erro').html(status);
            $('#listSoiCauTX').hide();
        } else {
            $('#listSoiCauTX').show();
            $('#tx_game_erro').hide();
        }
    }

    luckyDiceLogic.prototype.GetPointRutLoc = function () {
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.Url_GetPointRutLoc,
            crossDomain: true,
            xhrFields: {
                withCredentials: true
            },
            success: function (data) {
                LuckyDiceGame.totalPointTl = data.Point;
                if (data.Point >= 0) {
                    $("#tx_luot_rutLoc").html('Báº¡n cĂ²n<br> <i class="tx_mau_rut">' + data.Point + ' lÆ°á»£t</i> rĂºt lá»™c');

                    if (LuckyDiceGame.intevalCountDownTl) {
                        clearInterval(LuckyDiceGame.intevalCountDownTl);
                    }
                    LuckyDiceGame.isInEvent = data.IsIntimeEv;
                    LuckyDiceGame.timeLeftTl = data.SecondLeft;
                    if (LuckyDiceGame.timeLeftTl > 60) {
                        LuckyDiceGame.timeLeftTl = LuckyDiceGame.timeLeftTl - 60;
                        LuckyDiceGame.isInEvent = false;
                    } else {
                        LuckyDiceGame.isInEvent = true;
                    }
                    LuckyDiceGame.intevalCountDownTl = setInterval(function () {
                        var minute = Math.floor(LuckyDiceGame.timeLeftTl / 60);
                        var minutes = minute;
                        if (minute < 10) {
                            minutes = "0" + minute;
                        }
                        var second = Math.floor(LuckyDiceGame.timeLeftTl % 60);
                        var seconds = second;
                        if (second < 10) {
                            seconds = "0" + second;
                        }
                        $("#tx_time_rutloc").html(minutes + ":" + seconds);
                        LuckyDiceGame.timeLeftTl--;
                        if (LuckyDiceGame.timeLeftTl <= 0 && !LuckyDiceGame.isInEvent) {
                            LuckyDiceGame.isInEvent = true;
                            LuckyDiceGame.timeLeftTl = 60;
                            if (LuckyDiceGame.intevalCountDownTl) {
                                clearInterval(LuckyDiceGame.intevalCountDownTl);
                            }
                            LuckyDiceGame.GetPointRutLoc();
                        }

                        if (LuckyDiceGame.timeLeftTl <= 0 && LuckyDiceGame.isInEvent) {
                            setTimeout(function () {
                                LuckyDiceGame.GetResultRutLoc();
                            }, 10000)
                            if (LuckyDiceGame.intevalCountDownTl) {
                                clearInterval(LuckyDiceGame.intevalCountDownTl);
                            }
                            LuckyDiceGame.GetPointRutLoc();
                        }
                    }, 1000);
                }
            }
        });
    }

    luckyDiceLogic.prototype.GetResultRutLoc = function () {
        if (LuckyDiceGame.dkRutLoc <= 0) {
            return;
        }
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.Url_GetResultRutLoc,
            crossDomain: true,
            xhrFields: {
                withCredentials: true
            },
            success: function (data) {
                if (data.PrizeValue >= 0) {
                    LuckyDiceGame.ShowPopupStatus('ChĂºc má»«ng báº¡n Ä‘Æ°á»£c nháº­n ' + LuckyDiceGame.FormatNumber(data.PrizeValue) + "Sao tá»« tĂ­nh nÄƒng rĂºt lá»™c. <br/>Tham gia chÆ¡i TaXi Ä‘á»ƒ nháº­n Ä‘Æ°á»£c may máº¯n hÆ¡n nhĂ©!")
                } else {
                    LuckyDiceGame.ShowPopupStatus('RĂºt lá»™c khĂ´ng thĂ nh cĂ´ng! <br>ChĂºc báº¡n may máº¯n láº§n sau nhĂ©!');
                }
            }
        }).done(function () {
            LuckyDiceGame.dkRutLoc = 0;
        });
    }

    luckyDiceLogic.prototype.SelectRutLoc = function () {
        if (!this.isInEvent) {
            LuckyDiceGame.ShowPopupStatus('RĂºt lá»™c KHĂ”NG thĂ nh cĂ´ng.!<br/>Chá» 1p cuá»‘i cĂ¹ng nhĂ©!');
            return;
        } else if (this.totalPointTl <= 0) {
            LuckyDiceGame.ShowPopupStatus('Báº¡n Ä‘ang cĂ³ 0 láº§n rĂºt lá»™c.<br/>HĂ£y tham gia chÆ¡i TĂ i Xá»‰u Ä‘á»ƒ kiáº¿m lÆ°á»£t rĂºt');
            return;
        } else {
            $.ajax({
                type: "GET",
                url: luckyDiceConfig.Url_SelectRutLoc,
                crossDomain: true,
                xhrFields: {
                    withCredentials: true
                },
                success: function (data) {
                    if (data.Point >= 0) {
                        $("#tx_luot_rutLoc").html('Báº¡n cĂ²n<br> <i class="tx_mau_rut">' + data.Point + ' lÆ°á»£t</i> rĂºt lá»™c');
                    }
                    if (data.PrizeValue >= 0) {
                        LuckyDiceGame.dkRutLoc = 1;
                        LuckyDiceGame.ShowPopupStatus('ÄÄƒng kĂ½ rĂºt lá»™c thĂ nh cĂ´ng!<br> Vui lĂ²ng Ä‘á»£i sau 30s há»‡ thá»‘ng sáº½ tráº£ káº¿t quáº£ nhĂ©!');

                    } else {
                        LuckyDiceGame.ShowPopupStatus('ÄÄƒng kĂ½ rĂºt lá»™c khĂ´ng thĂ nh cĂ´ng! <br>Xin vui lĂ²ng thá»­ láº¡i!');
                    }
                }
            });
        }
    }

    luckyDiceLogic.prototype.GetVinhDanhTanLocMarquee = function () {
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.Url_GetVinhDanhTanLocMarquee,
            crossDomain: true,
            xhrFields: {
                withCredentials: true
            },
            success: function (data) {

                if (data && data.ListVinhDanh) {
                    var html = '';
                    for (var i = 0; i < data.ListVinhDanh.length; i++) {
                        html += 'Äáº¡i gia <i class="tx_mau_text_chuchay">' + data.ListVinhDanh[i].AccountName + '</i> Ä‘Ă£ tĂ¡n lá»™c <i class="tx_mau_text_chuchay1">' + LuckyDiceGame.FormatNumber(data.ListVinhDanh[i].PrizeValue) + ' Sao</i> ';
                    }
                    $("#tx_marqueVdTanLoc").html(html);
                }
            }
        });
    }

    luckyDiceLogic.prototype.SetBetLuckyDice = function () {
        var that = this;
        if (this.isBettingTx) { return; }
        else {
            var betOver = parseInt($("#input_tai_money").val().replace(/\./g, '')) || 0;
            var betUnder = parseInt($("#input_xiu_money").val().replace(/\./g, '')) || 0;
            if ((betOver == 0 && betUnder == 0)) {
                this.ShowStatus(1, "Vui lĂ²ng Ä‘áº·t cá»­a");
            } else if ((betOver > 0 && betUnder > 0)) {
                this.ShowStatus(1, "KhĂ´ng Ä‘áº·t 2 cá»­a má»™t phiĂªn");
            } else {
                var betType = this.isRoom;
                var locationId = (betOver > 0 ? 2 : 1);
                var betValue = (betOver > 0 ? betOver : betUnder);

                this.isBettingTx = true;
                LuckyDiceGame.gameLuckyDiceHub.server.setBet(betType, locationId, betValue).done(function (responseStatus) {
                    that.isBettingTx = false;
                    if (responseStatus >= 0) {
                        $("#input_tai_money").val('');
                        $("#input_xiu_money").val('');
                        $('.tipBet').text('0');
                        LuckyDiceGame.ShowStatus(3, "Äáº·t cá»­a thĂ nh cĂ´ng");
                        LuckyDiceGame.isEnter = true;
                    } else {
                        switch (responseStatus) {
                            case -207: LuckyDiceGame.ShowStatus(1, "Háº¿t thá»i gian Ä‘áº·t cá»­a"); console.log('het thoi gian dat cua'); return;
                            case -208: LuckyDiceGame.ShowStatus(1, "KhĂ´ng Ä‘áº·t 2 cá»­a má»™t phiĂªn"); console.log('dat 2 cua trong mot phong'); return;
                            case -212: LuckyDiceGame.ShowStatus(1, "GiĂ¡ trá»‹ Ä‘áº·t cá»­a khĂ´ng há»£p lá»‡"); console.log('gia tri dat cua khong hop le <0 > 2tr'); return;
                            case -232: LuckyDiceGame.ShowStatus(1, "Cá»­a Ä‘Äƒt khĂ´ng há»£p lá»‡"); console.log(data.responseStatus); return;
                            case -99: LuckyDiceGame.ShowStatus(1, "Há»‡ thá»‘ng giĂ¡n Ä‘oáº¡n"); console.log(data.responseStatus); return;
                            case -51: LuckyDiceGame.ShowStatus(1, "Sá»‘ dÆ° khĂ´ng Ä‘á»§"); console.log(data.responseStatus); return;
                            case -48: Util.showMessage("Game Ä‘Ă£ bá»‹ khĂ³a, vui lĂ²ng má»Ÿ khĂ³a Ä‘á»ƒ tiáº¿p tá»¥c giao dá»‹ch"); LuckyDiceGame.ShowStatus(1, "Game Ä‘Ă£ bá»‹ khĂ³a"); console.log(data.responseStatus); return;
                            default: LuckyDiceGame.ShowStatus(1, "Há»‡ thá»‘ng giĂ¡n Ä‘oáº¡n"); console.log('err: ' + data.responseStatus); return;
                        }
                    }

                }).fail(function () {
                    that.isBettingTx = false;
                });
            }
        }
    }

    luckyDiceLogic.prototype.StartGetResultAcc = function () {
        LuckyDiceGame.gameLuckyDiceHub.server.GetAccountResult(LuckyDiceGame.sessionNow).done(function (data) { console.log(1) });
        setTimeout(function () {
            if (LuckyDiceGame.isMoneyResult) {
                LuckyDiceGame.gameLuckyDiceHub.server.GetAccountResult(LuckyDiceGame.sessionNow).done(function (data) { console.log(2); });
            }
        }, 5000);
        setTimeout(function () {
            if (LuckyDiceGame.isMoneyResult) {
                LuckyDiceGame.gameLuckyDiceHub.server.GetAccountResult(LuckyDiceGame.sessionNow).done(function (data) { console.log(3); });
            }
        }, 10000);
        setTimeout(function () {
            if (LuckyDiceGame.isMoneyResult) {
                LuckyDiceGame.gameLuckyDiceHub.server.GetAccountResult(LuckyDiceGame.sessionNow).done(function (data) { console.log(4); });
            }
        }, 15000);
    }

    luckyDiceLogic.prototype.RunTimerTX = function () {
        if ($('#sessionidTX').text() == 'PhiĂªn: 0000') {
            LuckyDiceGame.gameLuckyDiceHub.server.getCurrentRooms(LuckyDiceGame.isRoom).done(function () { }).fail();
        }

        if (typeof LuckyDiceGame.currentSession == 'undefined') {
            return;
        } else {
            var tickWait = LuckyDiceGame.tickWait;
            var tickBet = LuckyDiceGame.tickBet;
            if (tickWait > 0) {
                tickWait--;
                $('#tx_luot_rutLoc').css('padding-top', '0px');
                $('#tx_game_erro').css('margin-top', '5px');
                LuckyDiceGame.tickWait = tickWait;

                if (tickWait == 1) LuckyDiceGame.StartGame();
                //if (tickWait == 20 && LuckyDiceGame.isEnter == true) LuckyDiceGame.StartGetResultAcc();
                if (tickWait == 20) {
                    if (LuckyDiceGame.isEnter == true) {
                        LuckyDiceGame.StartGetResultAcc();
                    } else {
                        if ($("#allGameLuckyDice").css('display') == 'none' && LuckyDiceGame.dice01 != 0) {
                            $('#prizebet').css('top', '22px');
                            $('#prizebet').css('opacity', '1');
                            $('#prizebet').show();
                            var numberResult = LuckyDiceGame.dice01 + LuckyDiceGame.dice02 + LuckyDiceGame.dice03;
                            $('#prizebet').html(numberResult > 10 ? ('TĂ i: ' + numberResult) : ('Xá»‰u: ' + numberResult));
                            $('#prizebet').css('left', '-39px');
                            $('#prizebet').animate({ top: '0px', opacity: 0 }, 5000);
                        }
                    }
                }


                if (tickWait == 14 && $('#tx_bat_nan').css('display') == 'block') LuckyDiceGame.StopEffectOpenBowl();
                if (tickWait < 16) LuckyDiceGame.SetAllowbet(true);

                $('#runTimer_TX').html(LuckyDiceGame.formatTime(tickWait));
                $('#runTimer_TX').css('color', 'white');
                $('#time').text(LuckyDiceGame.formatTime(tickWait));
                $('#time').css('color', '#fff');
            } else {
                if (tickBet > 0) {
                    tickBet--;
                    LuckyDiceGame.tickBet = tickBet;
                }
                LuckyDiceGame.textTime.alpha = 1;
                LuckyDiceGame.bg_bitmap.alpha = 1;
                LuckyDiceGame.stageCanvas.getChildAt(1).alpha = 0;
                $('#tx_cua_tai').removeClass('animated');
                $('#tx_cua_xiu').removeClass('animated');
                LuckyDiceGame.containerResult.removeAllChildren();
                $('#tx_totalDiemPhien').hide();
                $('#runTimer_TX').html(' ');
                $('#tx_luot_rutLoc').css('padding-top', '65px');
                $('#tx_game_erro').css('margin-top', '35px');
                LuckyDiceGame.textTime.text = LuckyDiceGame.formatTime(tickBet);
                $('#time').text(LuckyDiceGame.formatTime(tickBet));

                if (tickBet > 5) {
                    LuckyDiceGame.SetAllowbet(true);
                    LuckyDiceGame.textTime.color = "#ffc600";
                    $('#time').css('color', '#ffc600');
                } else {
                    LuckyDiceGame.SetAllowbet(false);
                    LuckyDiceGame.textTime.color = "#FF0100";
                    $('#time').css('color', '#ff0100');
                }

                if (tickBet == 0) {
                    LuckyDiceGame.isBet = false;
                }
            }
        }
    }

    luckyDiceLogic.prototype.TDFormatDateTimeHMSZ = function (date) {
        var str = date.split("T");
        var arrDate = str[1].split(":");
        var h = arrDate[0];
        var m = arrDate[1];
        var s = arrDate[2];
        s = s.substring(0, 2);
        var s1 = s < 10 ? "0" + Math.floor(s) : Math.floor(s);
        return h + ":" + m + ":" + s1;
    }

    luckyDiceLogic.prototype.SetAllowbet = function (bool) {
        LuckyDiceGame.isBet = bool;
        if (bool) {
            $("#input_tai_money").removeAttr('disabled');
            $("#input_xiu_money").removeAttr('disabled');
        } else {
            $("#input_tai_money").attr('disabled', 'disabled');
            $("#input_xiu_money").attr('disabled', 'disabled');
        }
    }

    luckyDiceLogic.prototype.StartGame = function () {
        this.isEnter = false;
        this.isMoneyResult = true;
        $('#tx_totalDiemPhien').hide();
        LuckyDiceGame.stageCanvas.getChildAt(1).alpha = 0;
        this.textTime.alpha = 1;
        this.bg_bitmap.alpha = 1;
        this.containerResult.removeAllChildren();
        $('#tx_cua_tai').removeClass('animated');
        $('#tx_cua_xiu').removeClass('animated');
        $("#input_tai_money_bottom").html("0");
        $("#input_xiu_money_bottom").html("0");
        $('#tx_money_xiu').html(0);
        $('#tx_poeple_xiu').html(0);
        $('#tx_money_tai').html(0);
        $('#tx_poeple_tai').html(0);
        setTimeout(function () {
            LuckyDiceGame.gameLuckyDiceHub.server.getCurrentRooms(LuckyDiceGame.isRoom).done(function () { }).fail();
        }, 5000);
    }

    luckyDiceLogic.prototype.ReplaceStringHistory = function (string) {
        string = string.replace(/\ /g, '-');
        string = string.replace(/\---/g, '-');
        string = string.replace(/\--/g, ' ');
        return string;
    }

    luckyDiceLogic.prototype.ChangeMoney = function (e) {        
        e.value = e.value.replace(/[^0-9\.]/g, '');
        e.value = e.value.replace(/\./g, '');
        e.value = LuckyDiceGame.FormatNumber(e.value);
    }

    luckyDiceLogic.prototype.inputKeypress = function (keycode) {
        if (keycode == 13) {
            LuckyDiceGame.SetBetLuckyDice();
        }
    }

    luckyDiceLogic.prototype.ShowPopupStatus = function (msg) {
        $.ajax({
            type: "GET",
            url: luckyDiceConfig.Url_Root + 'MiniGameLuckyDice/PopupStatus',
            success: function (data) {
                LuckyDiceGame.SetPopup(480, 315, data);
                $('#tx_status_show').html(msg);
            },
            fail: function (fail) {
                console.log('loi nhe');
            }
        });
    }

    luckyDiceLogic.prototype.OnFocusInputMoneyTai = function (e) {
        e.placeholder = '';
        if (e.value == '0' || e.value == '')
            e.value = '';
        if (LuckyDiceGame.isBet) {
            $('#input_tai_money_btn').show();
            $('#input_xiu_money_btn').hide();
        }
    }

    luckyDiceLogic.prototype.OnFocusInputMoneyXiu = function (e) {
        e.placeholder = '';
        if (e.value == '0' || e.value == '')
            e.value = '';
        if (LuckyDiceGame.isBet) {
            $('#input_tai_money_btn').hide();
            $('#input_xiu_money_btn').show();
        }
    }

    luckyDiceLogic.prototype.OnBlurInputMoney = function (e) {
        e.placeholder = 'Nháº­p sá»‘';
        if (e.value == '') {
            e.value = '';
        }
        $('#input_tai_money_btn').hide();
        $('#input_xiu_money_btn').hide();
    }

    luckyDiceLogic.prototype.FormatNumberTaiXiu = function (stringNumber) {
        stringNumber += '';
        var x = stringNumber.split(',');
        var x1 = x[0];

        return this.FormatNumber(parseInt(x1 / 1000)) + ' K';
    }

    luckyDiceLogic.prototype.FormatNumber = function (stringNumber) {
        stringNumber += '';
        var x = stringNumber.split(',');
        var x1 = x[0];
        var x2 = x.length > 1 ? ',' + x[1] : '';
        var rgx = /(\d+)(\d{3})/;
        while (rgx.test(x1))
            x1 = x1.replace(rgx, '$1' + '.' + '$2');

        return x1 + x2;
    }

    luckyDiceLogic.prototype.formatTime = function (inputTime) {
        var secNumb = parseInt(inputTime);
        var hours = Math.floor((secNumb) / 3600);
        var minutes = Math.floor((secNumb - hours * 3600) / 60);
        var seconds = secNumb - (minutes * 60);

        if (hours < 10) hours = "0" + hours;

        if (minutes < 10) minutes = "0" + minutes;

        if (seconds < 10) seconds = "0" + seconds;

        return minutes + ':' + seconds;
    }

    luckyDiceLogic.prototype.formDateTimehms = function (date) {
        date = date.replace(/\-/g, '\/').replace(/[T|Z]/g, ' ');
        if (date.indexOf('.') > 0)
            date = date.substring(0, date.indexOf('.'));
        var d = new Date(date);
        var curr_date = d.getDate();
        var curr_month = d.getMonth() + 1;
        var curr_year = d.getFullYear();
        var _hour = d.getHours();
        var _minute = d.getMinutes();
        var _second = d.getSeconds();
        if (curr_date < 10) curr_date = "0" + curr_date;
        if (curr_month < 10) curr_month = "0" + curr_month;
        if (_hour < 10) _hour = "0" + _hour;
        if (_minute < 10) _minute = "0" + _minute;
        return curr_date + "/" + curr_month
            + "/" + curr_year + " " + _hour + ":" + _minute;
    }

    scope.LuckyDiceLogic = luckyDiceLogic;
})(window, $);

$(document).ready(function () {
    LuckyDiceGame = new window.LuckyDiceLogic();
    LuckyDiceGame.ShowLuckyDice();
});