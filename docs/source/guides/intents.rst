Intents
=======

:class:`IntentFlags <mizuki.flags.IntentFlags>` is the library's implementation of Gateway Intents. Intents can be used to specify which events your bot will receive from Discord.

Intents are of two type:
    
- **Standard Intents:** These intents can be passed without additional setup or configuration. You can use :meth:`IntentFlags.standard() <mizuki.flags.IntentFlags.standard>` to enable all standard flags at once.

- **Privileged Intents:** These intents require their specific toggles to be enabled in the Developer Portal. You can use :meth:`IntentFlags.all() <mizuki.flags.IntentFlags.all>` to enable all standard as well as privileged flags.

.. note::
    
    If your bot has less than 10,000 users, then it can use the Privileged Intents freely. When your bot reaches more than 10,000 users, it needs to apply for those intents. `Read more here <https://support-dev.discord.com/hc/en-us/sections/5324794669207-Privileged-Gateway-Intents>`_.
    
    Most of the time, you will not need to use any of the privileged intents. `Click here to learn more <https://docs.discord.com/developers/gateway/you-might-not-need-a-privileged-intent>`_.
    

Each Intent can be associated with a set of event and if an event is not listed below, it means that is sent regardless of what intents you pass.
    
.. dropdown:: Gateway Intents

    .. code-block::

        GUILDS (1 << 0)
          - GUILD_CREATE
          - GUILD_UPDATE
          - GUILD_DELETE
          - GUILD_ROLE_CREATE
          - GUILD_ROLE_UPDATE
          - GUILD_ROLE_DELETE
          - CHANNEL_CREATE
          - CHANNEL_UPDATE
          - CHANNEL_DELETE
          - CHANNEL_PINS_UPDATE
          - THREAD_CREATE
          - THREAD_UPDATE
          - THREAD_DELETE
          - THREAD_LIST_SYNC
          - THREAD_MEMBER_UPDATE *
          - THREAD_MEMBERS_UPDATE
          - STAGE_INSTANCE_CREATE
          - STAGE_INSTANCE_UPDATE
          - STAGE_INSTANCE_DELETE
          - VOICE_CHANNEL_STATUS_UPDATE
          - VOICE_CHANNEL_START_TIME_UPDATE
        
        GUILD_MEMBERS (1 << 1)
          - GUILD_MEMBER_ADD
          - GUILD_MEMBER_UPDATE **
          - GUILD_MEMBER_REMOVE
          - THREAD_MEMBERS_UPDATE *
        
        GUILD_MODERATION (1 << 2)
          - GUILD_AUDIT_LOG_ENTRY_CREATE
          - GUILD_BAN_ADD
          - GUILD_BAN_REMOVE
        
        GUILD_EXPRESSIONS (1 << 3)
          - GUILD_EMOJIS_UPDATE
          - GUILD_STICKERS_UPDATE
          - GUILD_SOUNDBOARD_SOUND_CREATE
          - GUILD_SOUNDBOARD_SOUND_UPDATE
          - GUILD_SOUNDBOARD_SOUND_DELETE
          - GUILD_SOUNDBOARD_SOUNDS_UPDATE
        
        GUILD_INTEGRATIONS (1 << 4)
          - GUILD_INTEGRATIONS_UPDATE
          - INTEGRATION_CREATE
          - INTEGRATION_UPDATE
          - INTEGRATION_DELETE
        
        GUILD_WEBHOOKS (1 << 5)
          - WEBHOOKS_UPDATE
        
        GUILD_INVITES (1 << 6)
          - INVITE_CREATE
          - INVITE_DELETE
        
        GUILD_VOICE_STATES (1 << 7)
          - VOICE_CHANNEL_EFFECT_SEND
          - VOICE_STATE_UPDATE
        
        GUILD_PRESENCES (1 << 8)
          - PRESENCE_UPDATE
        
        GUILD_MESSAGES (1 << 9)
          - MESSAGE_CREATE
          - MESSAGE_UPDATE
          - MESSAGE_DELETE
          - MESSAGE_DELETE_BULK
        
        GUILD_MESSAGE_REACTIONS (1 << 10)
          - MESSAGE_REACTION_ADD
          - MESSAGE_REACTION_REMOVE
          - MESSAGE_REACTION_REMOVE_ALL
          - MESSAGE_REACTION_REMOVE_EMOJI
        
        GUILD_MESSAGE_TYPING (1 << 11)
          - TYPING_START
        
        DIRECT_MESSAGES (1 << 12)
          - MESSAGE_CREATE
          - MESSAGE_UPDATE
          - MESSAGE_DELETE
          - CHANNEL_PINS_UPDATE
        
        DIRECT_MESSAGE_REACTIONS (1 << 13)
          - MESSAGE_REACTION_ADD
          - MESSAGE_REACTION_REMOVE
          - MESSAGE_REACTION_REMOVE_ALL
          - MESSAGE_REACTION_REMOVE_EMOJI
        
        DIRECT_MESSAGE_TYPING (1 << 14)
          - TYPING_START
        
        MESSAGE_CONTENT (1 << 15) ***
        
        GUILD_SCHEDULED_EVENTS (1 << 16)
          - GUILD_SCHEDULED_EVENT_CREATE
          - GUILD_SCHEDULED_EVENT_UPDATE
          - GUILD_SCHEDULED_EVENT_DELETE
          - GUILD_SCHEDULED_EVENT_USER_ADD
          - GUILD_SCHEDULED_EVENT_USER_REMOVE
        
        AUTO_MODERATION_CONFIGURATION (1 << 20)
          - AUTO_MODERATION_RULE_CREATE
          - AUTO_MODERATION_RULE_UPDATE
          - AUTO_MODERATION_RULE_DELETE
        
        AUTO_MODERATION_EXECUTION (1 << 21)
          - AUTO_MODERATION_ACTION_EXECUTION
        
        GUILD_MESSAGE_POLLS (1 << 24)
          - MESSAGE_POLL_VOTE_ADD
          - MESSAGE_POLL_VOTE_REMOVE
        
        DIRECT_MESSAGE_POLLS (1 << 25)
          - MESSAGE_POLL_VOTE_ADD
          - MESSAGE_POLL_VOTE_REMOVE
  
          
    \* ``THREAD_MEMBERS_UPDATE`` is only sent for the current bot (when it is added to or removed from a thread) unless ``GUILD_MEMBERS`` intent is enabled.
    
    ** ``GUILD_MEMBER_UPDATE`` is always sent for the current user updates regardless of intents.
        
        
    \*** ``MESSAGE_CREATE`` events are still sent when you have ``GUILD_MESSAGES`` enabled and ``MESSAGE_CONTENT`` disabled, but they will not contain content, embeds, components, attachments and polls unless you also enable ``MESSAGE_CONTENT``.
        
        However, you do not need this intent to access the previously mentioned fields if the message meets one of the following conditions:
            
        - The message mentions the bot.
        - The message replies to a message sent by the bot.
        - The message is sent in a DM to the bot.
        - The message is sent by the bot.
        

As your bot grows, try to enable only the intents it needs. For example, a bot that only responds to slash commands typically requires far fewer intents than a moderation bot.

Examples of explicitly specifying intents:
    
.. code-block:: python

    bot = mizuki.Bot(
        intents=(
            mizuki.IntentFlags.GUILDS
            | mizuki.IntentFlags.DIRECT_MESSAGES
            | mizuki.IntentFlags.GUILD_MESSAGES
            | mizuki.IntentFlags.MESSAGE_CONTENT
        )
    )