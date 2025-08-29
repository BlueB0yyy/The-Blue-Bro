from code.const import BG_HEIGHT
from code.enemy import Enemy
from code.entity import Entity
from code.player import Player


class EntityMediator:

    # Verificar se caiu do mapa
    @staticmethod
    def __verify_collision_window(ent: Entity):
        # Se for Player ou Enemy
        if isinstance(ent, Enemy) or isinstance (ent, Player):
            # se o topo do rect for maior que a janela
            if ent.rect.top >= BG_HEIGHT:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True
            #print('teste')
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        #Fazer métodos se for entidade atacando

        #Se tiver interação
        if valid_interaction:
            if isinstance(ent1, Player) and isinstance(ent2, Enemy):
                if (ent1.rect.right > ent2.rect.left and
                        ent1.rect.left < ent2.rect.right):
                    # Pulo na cabeça
                    if (ent1.rect.bottom <= ent2.rect.top and
                            getattr(ent1, "vel_y", 1) > 0):
                        ent2.health -= ent1.damage
                        ent2.kill = ent1.name
                        ent1.vel_y = -20
                        return
                    return
            elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
                if (ent2.rect.bottom <= ent1.rect.top
                        and getattr(ent2, "vel_y", 1) > 0):
                    ent1.health -= ent2.damage
                    ent1.kill = ent2.name
                    ent2.vel_y = -20
                    return

                # Caso contrário, colisão normal (ambos perdem vida)
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.kill = ent2.name
                ent2.kill = ent1.name


    @staticmethod
    def verify_health(entity_list: list[Entity], ):
        killed = False
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__stop_score(ent, entity_list)
                    killed = True
                entity_list.remove(ent)
        return killed

    @staticmethod
    def __stop_score(enemy: Enemy, entity_list: list[Entity]):
        pass
        if enemy.kill == 'Player':
            for ent in entity_list:
                ent.score -= enemy.score #Um valor para cada tipo de inimigo morto
