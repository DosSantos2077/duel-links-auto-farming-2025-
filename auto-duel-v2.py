from imagesearch import *
import pyautogui as pa

folder = "./image/"
character = "yami_yugi"
duel_counter = 0

max_duel = int(input("How many duels?: "))

while True:
    if duel_counter == max_duel:
        break

    # Find gate button
    #pos = imagesearch_loop(folder+"gate.png", 1)
    #print("Gate button found : ", pos[0], pos[1])

    # Click gate button
    #if pos[0] != -1:
        #click_image(folder+"gate.png", pos, "left", 2)
    #print("Gate button clicked")

    # Find duel button #1
    pos = imagesearch_loop(folder+"duel.png", 0.3)
    print("Duel button found : ", pos[0], pos[1])

    # Click duel button #1
    if pos[0] != -1:
        click_image(folder+"duel.png", pos, "left", 0.5)
    print("Duel button clicked")

    # Find dialogue arrow #1
    pos = imagesearch_loop(folder+"dialogue_arrow.png", 0.3)
    print("dialogue arrow found : ", pos[0], pos[1])

    # Click dialogue arrow #1
    if pos[0] != -1:
        click_image(folder+"dialogue_arrow.png", pos, "left", 0.5)
    print("dialogue arrow clicked")

    # Find duel button #2
    pos = imagesearch_loop(folder+"duel.png", 0.3)
    print("Duel button found : ", pos[0], pos[1])

    # Click duel button #2
    if pos[0] != -1:
        click_image(folder+"duel.png", pos, "left", 0.5)
    print("Duel button clicked")

    pos = imagesearch_loop_timeout(folder+"menu.png", 0.1, 120.0)
    if pos[0] > -1:
        for i in range(7):
            pa.click(x=964, y=549)
            time.sleep(0.1)
    else:
        break
    # print("Duel standby")

    # imagesearch_loop_timeout(folder+"main_phase.png", 0.1)
    print("Your main phase")

    main_phase_status = True
    battle_phase_status = False
    monster_exist = False

    while True:
        # Show action button periodically
        pa.click(x=620, y=820)
        # Speed up draw phase
        pos = imagesearch(folder+"draw_phase.png")
        if pos[0] > -1:
            for i in range(3):
                pa.click(x=620, y=820)
                time.sleep(0.05)
            time.sleep(1)
            for i in range(3):
                pa.click(x=620, y=820)
                time.sleep(0.05)

        
            
        
        init_x = 737
        pos_x = init_x
        init_y = 1034
        new_pos = 0
        counter = 0
        max_counter = 5
        recheck = False
        equip_counter = 0
        
        if main_phase_status:
            pos = imagesearch_loop_timeout(folder+"action.png", 0.1, 5.0)
            if pos[0] > -1:
                # Change to attack position if any
                if monster_exist:
                    monster = [958, 1084, 834]
                    monster_pos_y = 580

                    for monster_pos in monster:
                        pa.click(x=monster_pos, y=monster_pos_y)
                        pos = imagesearch_loop_timeout(folder+"action.png", 0.1, 1.5)
                        if pos[0] > -1:
                            pa.click(x=monster_pos, y=monster_pos_y)
                        pos = imagesearch_loop_timeout(folder+"change_to_attack_position.png", 0.1, 2.0)
                        if pos[0] > -1:
                            click_image(folder+"change_to_attack_position.png", pos, "left", 0.1)
                        pos = imagesearch_loop_timeout(folder+"flip_summon.png", 0.1, 2.0)
                        if pos[0] > -1:
                            click_image(folder+"flip_summon.png", pos, "left", 0.1)
                    # Bring back action button
                    pa.click(x=620, y=820)
                    
                while True:
                    pa.click(x=pos_x + new_pos, y=init_y)
                    time.sleep(0.1)
                    #pa.click(x=pos_x + new_pos, y=init_y)
                    #time.sleep(1)

                    
                    
                    pos = imagesearch(folder+"normal_summon.png")
                    # pos = imagesearch_loop_timeout(folder+"normal_summon.png", 0.1, 1)
                    if (pos[0] > -1):
                        click_image(folder+"normal_summon.png", pos, "left", 0.3)
                        # wait action button to be show
                        pa.click(x=620, y=820)
                        imagesearch_loop_timeout(folder+"action.png", 0.1, 10.0)
                        counter = 0
                        max_counter -= 1
                        monster_exist = True
                    
                    
                    #pos = imagesearch(folder+"set.png")
                    # pos = imagesearch_loop_timeout(folder+"set.png", 0.1, 1.0)
                    #if (pos[0] > -1):
                        #pos2 = imagesearch_loop_timeout(folder+"equip.png", 0.1, 1.0)
                        #if pos2[0] > -1:
                            #equip_counter += 1
                            #counter -= 1
                        #else:
                            #click_image(folder+"set.png", pos, "left", 0.2)
                            ## wait action button to be show
                            #pa.click(x=620, y=820)
                            #imagesearch_loop(folder+"action.png", 0.1)
                            #counter = 0
                            #max_counter -= 1
                    
                    if equip_counter > 0 and monster_exist:
                        recheck = True
                        # equip_counter = 0

                    new_pos += 55
        
                    if counter >= max_counter:
                        main_phase_status = False
                        if monster_exist:
                            battle_phase_status = True
                            
                        pa.click(x=620, y=820)

                        if recheck:
                            recheck = False
                            pos_x = init_x
                            new_pos = 100
                            counter = 0

                            equip_counter = 0
                        else:
                            break
                    
                    counter += 1
                    time.sleep(1)
            

        if battle_phase_status:
            # Find and click action button
            pos = imagesearch_loop_timeout(folder+"action.png", 0.1, 5.0)
            # print("Action button found : ", pos[0], pos[1])
            # Click action button
            if pos[0] > -1:
                click_image(folder+"action.png", pos, "left", 0.2)
                time.sleep(0.4)
                # print("Action button clicked")
                # Find Battle button
                pos = imagesearch_loop_timeout(folder+"battle_phase.png", 0.2, 5.0)
                # print("Battle button found : ", pos[0], pos[1])
                # Click Battle button
                if pos[0] > -1:
                    click_image(folder+"battle_phase.png", pos, "left", 0.3)
                    # print("Battle button clicked")

                    # Attack
                    monster = [958, 1084, 834]
                    monster_pos_y = 580

                    for monster_pos in monster:
                        pos = imagesearch_loop_timeout(folder+"action.png", 0.1, 30.0)
                        if pos[0] > -1:
                            pa.click(x=monster_pos, y=monster_pos_y)
                            pos = imagesearch_loop_timeout(folder+"attack.png", 0.2, 2.0)
                            if pos[0] > -1:
                                click_image(folder+"attack.png", pos, "left", 0.2)
                                # Confirm attack if there is more than 1 monster
                                pos = imagesearch_loop_timeout(folder+"confirm_disabled.png", 0.1, 2.0)
                                if pos[0] > -1:
                                    # Click card to activate
                                    pa.click(x=667, y=793) 
                                    pos = imagesearch(folder+"confirm_enabled.png")
                                    if pos[0] > -1:
                                        click_image(folder+"confirm_enabled.png", pos, "left", 0.2)
                else:
                    # Find end phase button
                    pos = imagesearch_loop_timeout(folder+"end_phase.png", 0.1, 2)
                    # print("End phase button found : ", pos[0], pos[1])
                    # Click end phase button
                    if pos[0] > -1:
                        click_image(folder+"end_phase.png", pos, "left", 0.2)
                        # print("End phase button clicked")

                battle_phase_status = False

        if not main_phase_status and not battle_phase_status:
            # main_phase_status = True
            pos = imagesearch_loop_timeout(folder+"action.png", 0.1, 2.0)
            # print("Action button found : ", pos[0], pos[1])
            # Click action button
            if pos[0] > -1:
                click_image(folder+"action.png", pos, "left", 0.2)
                # Find end phase button
                pos = imagesearch_loop_timeout(folder+"end_phase.png", 0.1, 2)
                # print("End phase button found : ", pos[0], pos[1])
                # Click end phase button
                if pos[0] > -1:
                    click_image(folder+"end_phase.png", pos, "left", 0.2)
                    # print("End phase button clicked")
                    main_phase_status = True
            
        # Check if duel finished
        pos = imagesearch(folder+"ok.png")
        if pos[0] > -1:
            duel_counter += 1
            print("isso")
            break

    for i in range(3):
        pa.click(x=960, y=832)
        time.sleep(0.1)
    time.sleep(0.2)
    print("Duel Finished : "+str(duel_counter))

    # Click ok button
    if pos[0] != -1:
        click_image(folder+"ok.png", pos, "left", 0.2)
    # print("OK button clicked")

    

    # Wait next button
    search = True
    while search:
        pos = imagesearch(folder+"next.png")
        if pos[0] != -1:
            search = False
        for i in range(3):
            # pa.click(x=960, y=832)
            pa.click(x=964, y=690)
            time.sleep(0.3)
        time.sleep(0.3)
    # print("Next button found")

    # Click next button
    if pos[0] != -1:
        click_image(folder+"next.png", pos, "left", 0.5)
    # print("Next button clicked")

    # Wait next button
    search = True
    while search:
        pos = imagesearch(folder+"next.png")
        if pos[0] != -1:
            search = False
        for i in range(3):
            # pa.click(x=960, y=832)
            pa.click(x=960, y=119)
            time.sleep(0.1)
        time.sleep(0.3)
    # print("Next button found")

    # Click next button
    if pos[0] != -1:
        click_image(folder+"next.png", pos, "left", 0.5)
    # print("Next button clicked")

    pos = imagesearch_loop_timeout(folder+"next.png", 0.1, 2)  

    if pos[0] != -1:
        click_image(folder+"next.png", pos, "left", 0.5)

    pos = imagesearch_loop_timeout(folder+"caps.png", 0.1, 2)

    while pos[0] != -1:
        pa.click(x=960, y=119)
        pos = imagesearch_loop_timeout(folder+"caps.png", 0.1, 2)

    pos = imagesearch_loop_timeout(folder+"get.png", 0.1, 2)

    if pos[0] != -1:
        pa.click(x=960, y=119)
        pos = imagesearch_loop_timeout(folder+"ok.png", 0.1, 2)  

        if pos[0] != -1:
            click_image(folder+"ok.png", pos, "left", 0.5)


    pos = imagesearch_loop_timeout(folder+"next.png", 0.1, 2)  

    if pos[0] != -1:
        click_image(folder+"next.png", pos, "left", 0.5)  

    # Find dialogue arrow #1
    pos = imagesearch_loop(folder+"dialogue_arrow.png", 0.3)
    print("dialogue arrow found : ", pos[0], pos[1])

    # Click dialogue arrow #1
    if pos[0] != -1:
        click_image(folder+"dialogue_arrow.png", pos, "left", 0.5)
    print("dialogue arrow clicked")

    if duel_counter == max_duel:
        pos = imagesearch_loop(folder+"exit_gate.png", 0.3)
        print("Exit button found : ", pos[0], pos[1])

        # Click exit gate arrow button 
        if pos[0] != -1:
            click_image(folder+"exit_gate.png", pos, "left", 0.5)
        break


#while True:
    #pos = imagesearch_loop_timeout(folder+"auto_1d3.png", 0.3, 10, 7.0)
    #print("auto duel found : ", pos[0], pos[1])

    # Click arrow button to change location
    #if pos[0] != -1:
      #  click_image(folder+"auto_1d3.png", pos, "left", 0.5)
     #   print("auto_duel clicked")

    #pos = imagesearch_loop(folder+"arrow.png", 0.3)
    #print("Arrow button found : ", pos[0], pos[1])

    # Click arrow button to change location
   # if pos[0] != -1:
     #   click_image(folder+"arrow.png", pos, "left", 0.5)
    #print("Arrow button clicked")




