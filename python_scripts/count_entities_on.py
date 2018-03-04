on = 0
for entity_id in hass.states.entity_ids('light'):
    state = hass.states.get(entity_id)
    if state.state == 'on':
        on = on + 1
for entity_id in hass.states.entity_ids('switch'):
    state = hass.states.get(entity_id)
    if state.state == 'on':
        on = on + 1
hass.states.set('sensor.entities_on', on, {
    'friendly_name': 'Påslagna'
})
